import argparse
import json
import os

import boto3

SRC_BUCKET = 'its-live-open'
DST_BUCKET = 'its-live-data'

JOB_QUEUE = 'opendata-transfer-job-queue'
JOB_DEFINITION = 'opendata-transfer-job-definition'

os.environ['AWS_PROFILE'] = 'its-live'

batch = boto3.client('batch')
s3 = boto3.client('s3')


def get_sub_prefixes(prefix: str) -> list[str]:
    sub_prefixes = s3.list_objects_v2(
        Bucket=SRC_BUCKET,
        Prefix=prefix,
        Delimiter='/',
    )['CommonPrefixes']
    return [prefix['Prefix'] for prefix in sub_prefixes]


def get_batch_jobs() -> tuple[list[str], list[str]]:
    # Returns names of SUCCEEDED jobs and names of in-progress jobs

    params = {
        'jobQueue': JOB_QUEUE,
        'maxResults': 100,
        'filters': [{'name': 'JOB_NAME', 'values': ['final-transfer-*']}],
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


def submit_jobs(s3_prefixes: list[str], submit: bool) -> None:
    for count, prefix in enumerate(s3_prefixes, start=1):
        job_name = get_job_name(prefix)
        print(f'{count}/{len(s3_prefixes)} Submitting job {job_name}')
        if submit:
            batch.submit_job(
                jobName=job_name,
                jobQueue=JOB_QUEUE,
                jobDefinition=JOB_DEFINITION,
                parameters={
                    'src_bucket': SRC_BUCKET,
                    'dst_bucket': DST_BUCKET,
                    's3_prefix': prefix,
                }
            )


def get_job_name(s3_prefix: str) -> str:
    assert not s3_prefix.startswith('/')
    assert s3_prefix.endswith('/')
    return 'final-transfer-' + s3_prefix[:-1].replace('/', '--')


def parse_job_name(job_name: str) -> str:
    assert job_name.startswith('final-transfer-')
    return job_name.removeprefix('final-transfer-').replace('--', '/') + '/'


def main():
    # Tests:
    assert get_job_name('path/to/prefix/') == 'final-transfer-path--to--prefix'
    assert parse_job_name('final-transfer-path--to--prefix') == 'path/to/prefix/'

    parser = argparse.ArgumentParser()
    parser.add_argument('--submit', action='store_true', help='Do not submit jobs unless this option is given')
    args = parser.parse_args()

    if not args.submit:
        print('(DRY RUN)')

    with open('final-transfer-prefixes.json') as f:
        final_transfer_prefixes = json.load(f)

    prefixes = final_transfer_prefixes['prefixes']
    large_prefixes = final_transfer_prefixes['large_prefixes']

    for prefix in large_prefixes:
        prefixes.extend(get_sub_prefixes(prefix))

    prefixes.sort()
    print(f'Total prefixes: {len(prefixes)}')

    succeeded_jobs, in_progress_jobs = get_batch_jobs()

    succeeded_prefixes = {parse_job_name(job_name) for job_name in succeeded_jobs}
    print(f'Got {len(succeeded_jobs)} SUCCEEDED Batch jobs')

    if succeeded_prefixes == set(prefixes):
        print('All prefixes have transferred successfully')
        return

    in_progress_prefixes = {parse_job_name(job_name) for job_name in in_progress_jobs}
    print(f'Got {len(in_progress_jobs)} in-progress Batch jobs')

    prefixes_to_submit = [
        prefix for prefix in prefixes
        if prefix not in succeeded_prefixes
        and prefix not in in_progress_prefixes
    ]
    print(f'{len(prefixes_to_submit)} remaining prefixes to submit')

    submit_jobs(prefixes_to_submit, args.submit)


if __name__ == '__main__':
    main()
