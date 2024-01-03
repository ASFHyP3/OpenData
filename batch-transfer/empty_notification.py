import argparse
import logging
from time import sleep

import boto3
from tqdm.auto import tqdm

log = logging.getLogger('empty_notification.py')
s3_client = boto3.client('s3')
sns_client = boto3.client('sns')


def _bucket_is_empty(bucket: str) -> bool:
    results = s3_client.list_objects(Bucket=bucket, Delimiter='/')

    if len(results.get('CommonPrefixes', [])) > 0:
        log.debug(results['CommonPrefixes'])
        return False

    return True


def post_sns_message(topic_arn: str, bucket: str) -> dict:
    subject = f'{bucket} is empty!'
    message = f'The s3://{bucket} bucket is empty!'

    response = sns_client.publish(TopicArn=topic_arn, Message=message, Subject=subject)
    return response


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket', default='its-live-data', help='AWS S3 bucket to inspect')
    parser.add_argument('--sleep', type=int, default=60, help='seconds to sleep before inspections')
    parser.add_argument('--topic-arn', default='arn:aws:sns:us-west-2:050846374571:its-live-data-is-empty',
                        help='AWS SNS Topic to post "Bucket is empty" message to')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    log.info(f'Inspecting s3://{args.bucket} every {args.sleep} seconds')
    progress = tqdm()
    while not _bucket_is_empty(args.bucket):
        progress.update()
        sleep(args.sleep)

    log.info(f'Posting "Bucket is Empty" message to {args.topic_arn}')
    post_sns_message(topic_arn=args.topic_arn, bucket=args.bucket)


if __name__ == '__main__':
    main()
