import os
from datetime import datetime, timezone

import boto3

os.environ['AWS_PROFILE'] = 'its-live'

cloudwatch = boto3.client('cloudwatch')

data = cloudwatch.get_metric_statistics(
    Namespace='AWS/S3',
    MetricName='5xxErrors',
    Dimensions=[
        {'Name': 'BucketName', 'Value': 'its-live-project'},
        {'Name': 'FilterId', 'Value': 'EntireBucket'},
    ],
    StartTime=datetime(2023, 12, 13, 1, 10, tzinfo=timezone.utc),
    EndTime=datetime(2023, 12, 13, 1, 40, tzinfo=timezone.utc),
    Period=60,
    Statistics=['Sum'],
)['Datapoints']

data.sort(key=lambda x: x['Timestamp'])

for point in data:
    print(f'{point["Timestamp"].isoformat()} {int(point["Sum"]):10}')
