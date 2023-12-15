import argparse
import json
import logging
from pathlib import Path

import boto3

log = logging.getLogger('list_bucket_prefixes.py')
client = boto3.client('s3')


def _get_common_prefixes(bucket, prefix):
    results = client.list_objects(Bucket=bucket, Prefix=prefix, Delimiter='/')
    return {item['Prefix'] for item in results.get('CommonPrefixes', [])}


def list_bucket_prefixes(bucket: str, prefix: str = '', depth: int = 2):
    log.info(f'Listing prefixes for s3://{bucket}/{prefix} {depth} levels deep')

    all_prefixes = _get_common_prefixes(bucket, prefix)
    if depth > 0:
        sub_prefixes = set()
        for prefix in all_prefixes:
            sub_prefixes |= list_bucket_prefixes(bucket, prefix, depth=depth-1)
        all_prefixes |= sub_prefixes

    return all_prefixes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket', default='its-live-data', help='AWS S3 bucket to list prefixes for')
    parser.add_argument('--depth', type=int, default=2, help='How deep to list prefixes')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    all_prefixes = list_bucket_prefixes(**args.__dict__)
    Path(f'{args.bucket}.json').write_text(json.dumps(sorted(list(all_prefixes)), indent=2))


if __name__ == '__main__':
    main()
