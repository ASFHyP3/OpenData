# Adding a new dataset to AWS Open Data

First and foremost, you'll need to follow the AWS Onboarding Handbook for AWS Open Data. There is an archival copy available in the `docs/` [here](../docs/aws-onboarding-handbook-for-data-providers-en-US.pdf). 

The rest of this guide assumes you've followed at least steps 1-4 in the handbook, and are does not cover how to accomplish step 5 as it is likely dataset dependent. So, to summarize, the guide expects:
* a new/isolated AWS account for the dataset that you have admin access to using the `${AWS_PROFILE}` AWS profile
* an AWS S3 bucket (`${OPENDATA_BUCKET}`) to have already been created for the dataset in that account

## Create common files for datasets

TODO

## CI Setup

### GitHub Actions User 

In order to deploy the `README.html` and `index.html` for our datasets, there will need to be a `github-actions` user with permissions to write those files to the AWS S3 Open Data bucket. You can deploy the `asf-ci` which will set up that user and its permissions by running from the repository root:
```shell
aws cloudformation deploy --profile ${AWS_PROFILE} \
    --stack-name asf-ci \
    --template-file shared/ASF-ci-cf.yml \
    --capabilities CAPABILITY_NAMED_IAM \
    --parameter-overrides OpenDataBucketName=${OPENDATA_BUCKET}
```
>[!IMPORTANT]
> Note: This stack should only be deployed once per AWS account.

### GitGub Actions Environment

TODO
