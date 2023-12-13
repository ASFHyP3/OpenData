import argparse
import os
import time

import boto3

CLOUDWATCH_ALARM_NAME = 'asjohnston-its-live-project-5xx-errors'
JOB_QUEUE = 'opendata-transfer-job-queue'
JOB_DEFINITION = 'opendata-transfer-job-definition'
MAX_JOBS = 250

os.environ['AWS_PROFILE'] = 'its-live'

batch = boto3.client('batch')
s3 = boto3.client('s3')
cloudwatch = boto3.client('cloudwatch')


def alarm_5xx_errors() -> bool:
    return cloudwatch.describe_alarms(
        AlarmNames=[CLOUDWATCH_ALARM_NAME],
        AlarmTypes=['MetricAlarm'],
    )['MetricAlarms'][0]['StateValue'] == 'ALARM'


def get_sub_prefixes(src_bucket: str, prefix: str) -> list[str]:
    sub_prefixes = s3.list_objects_v2(
        Bucket=src_bucket,
        Prefix=prefix,
        Delimiter='/',
    )['CommonPrefixes']
    return sorted(prefix['Prefix'] for prefix in sub_prefixes)


def get_batch_jobs(job_name_prefix: str) -> tuple[list[str], list[str]]:
    # Returns names of SUCCEEDED jobs and names of in-progress jobs

    params = {
        'jobQueue': JOB_QUEUE,
        'maxResults': 100,
        'filters': [{'name': 'JOB_NAME', 'values': [job_name_prefix + '*']}],
    }

    jobs = []
    while True:
        response = batch.list_jobs(**params)
        jobs.extend(response['jobSummaryList'])
        if 'nextToken' not in response:
            break
        params['nextToken'] = response['nextToken']

    return (
        [job['jobName'] for job in jobs if job['status'] == 'SUCCEEDED'],
        [job['jobName'] for job in jobs if job['status'] not in ('SUCCEEDED', 'FAILED')],
    )


def submit_jobs(src_bucket: str, dst_bucket: str, s3_prefixes: list[str]) -> None:
    for count, prefix in enumerate(s3_prefixes, start=1):
        response = batch.submit_job(
            jobName=get_job_name(src_bucket, dst_bucket, prefix),
            jobQueue=JOB_QUEUE,
            jobDefinition=JOB_DEFINITION,
            parameters={
                'src_bucket': src_bucket,
                'dst_bucket': dst_bucket,
                's3_prefix': prefix
            }
        )
        print(f'{count}/{len(s3_prefixes)} Submitted job {response["jobName"]}')


def get_job_name(src_bucket: str, dst_bucket: str, s3_prefix: str) -> str:
    assert not s3_prefix.startswith('/')
    assert s3_prefix.endswith('/')
    prefix_name = s3_prefix[:-1].replace('/', '--')
    return '--'.join([src_bucket, dst_bucket, prefix_name])


def parse_job_name(job_name: str) -> tuple[str, str, str]:
    parts = job_name.split('--')
    src_bucket, dst_bucket = parts[:2]
    s3_prefix = '/'.join(parts[2:]) + '/'
    return src_bucket, dst_bucket, s3_prefix


def get_s3_prefix_from_job_name(job_name: str, expected_src: str, expected_dst: str) -> str:
    src_bucket, dst_bucket, s3_prefix = parse_job_name(job_name)
    assert src_bucket == expected_src
    assert dst_bucket == expected_dst
    return s3_prefix


def main():
    # Tests:
    assert get_job_name('foo', 'bar', 'path/to/file/') == 'foo--bar--path--to--file'
    assert parse_job_name('foo--bar--path--to--file') == ('foo', 'bar', 'path/to/file/')

    parser = argparse.ArgumentParser()
    parser.add_argument('src_bucket')
    # TODO: add more dst choices after adding more 5xx alarms (and don't use constant for alarm name)
    parser.add_argument('dst_bucket', choices=['its-live-project'])
    parser.add_argument('s3_prefix', help='Omit leading / but include trailing /, e.g. foo/bar/')
    args = parser.parse_args()

    prefixes = get_sub_prefixes(args.src_bucket, args.s3_prefix)
    print(f'Got {len(prefixes)} S3 sub-prefixes')

    job_name_prefix = get_job_name(args.src_bucket, args.dst_bucket, args.s3_prefix) + '--'
    print(f'Batch job name prefix: {job_name_prefix}')

    while True:
        succeeded_jobs, in_progress_jobs = get_batch_jobs(job_name_prefix)

        succeeded_prefixes = {
            get_s3_prefix_from_job_name(job_name, args.src_bucket, args.dst_bucket)
            for job_name in succeeded_jobs
        }
        print(f'Got {len(succeeded_jobs)} SUCCEEDED Batch jobs')

        if succeeded_prefixes == set(prefixes):
            print('All prefixes have transferred successfully')
            break

        in_progress_prefixes = {
            get_s3_prefix_from_job_name(job_name, args.src_bucket, args.dst_bucket)
            for job_name in in_progress_jobs
        }
        print(f'Got {len(in_progress_jobs)} in-progress Batch jobs')

        prefixes_to_submit = [
            prefix for prefix in prefixes
            if prefix not in succeeded_prefixes
            and prefix not in in_progress_prefixes
        ]
        print(f'{len(prefixes_to_submit)} remaining prefixes to submit')

        number_to_submit = min([MAX_JOBS - len(in_progress_jobs), 10])
        minutes = 1

        batch_of_prefixes = prefixes_to_submit[:number_to_submit]

        if not alarm_5xx_errors():
            submit_jobs(args.src_bucket, args.dst_bucket, batch_of_prefixes)
        else:
            print('Got alarm for 5xx errors, skipping submit jobs')

        print(f'Sleeping for {minutes} minutes...')

        time.sleep(minutes*60)

        # TODO error handling


if __name__ == '__main__':
    main()
