# Adding a new dataset to AWS Open Data

First and foremost, you'll need to follow the AWS Onboarding Handbook for AWS Open Data. There is an archival copy available in the `docs/` [here](../docs/aws-onboarding-handbook-for-data-providers-en-US.pdf). 

The rest of this guide assumes you've followed at least steps 1-4 in the handbook, and does *not* cover how to accomplish step 5 as it is likely dataset dependent. So, to summarize, the guide expects:
* a new/isolated AWS account for the dataset that you have admin access to using the `${AWS_PROFILE}` AWS profile
* an AWS S3 bucket (`${OPENDATA_BUCKET}`) to have already been created for the dataset in that account

## Create common files for datasets

First, create a directory with the same name as the AWS bucket to contain information about the dataset and how we manage it, as well as any directly managed files. from the repository root, run:
```shell
mkdir ${OPENDATA_BUCKET} && cd ${OPENDATA_BUCKET}
```

We expect each dataset to have in its S3 bucket a top-level:
* `README.html`, which describes the bucket (file) structure and data within. For ease of writing, an `${OPENDATA_BUCKET}/README.md` is generally created per-dataset and then transformed to this `README.html` and uploaded to the bucket via a GitHub Action, e.g., [deploy-asf-event-data-files.yml](../.github/workflows/deploy-asf-event-data-files.yml) 

* `index.html`, which allows browser-based exploration of the bucket. A template of this file is saved in the [`shared`](../shared) directory and generally created and uploaded via a GitHub Action, e.g., [deploy-asf-event-data-files.yml](../.github/workflows/deploy-asf-event-data-files.yml)

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
> Note: This stack should only be deployed once per AWS account. It is also a good idea to enable termination protection.

After the stack is created you'll need to create an AWS CLI access key for the `github-actions` user, which you will use in the next step.

### GitHub Actions Environment

We use a GitHub Actions Environment for each datasett to store the AWS access credentials necessary to deploy the common files.

First, create a new environment by following this link:
<https://github.com/ASFHyP3/OpenData/settings/environments/new>

and name it the same as the S3 bucket (`${OPENDATA_BUCKET}`). When configuring the environment you'll want to: 
1. set "Protected branches only" for the "Deployment branches and tags"
2. Add these environment secrets for the `github-actions` user:
   * `AWS_ACCESS_KEY_ID`
   * `AWS_SECRET_ACCESS_KEY`
   * `AWS_REGION` (typically `us-west-2`)

### Deployment action

Now, using [deploy-asf-event-data-files.yml](../.github/workflows/deploy-asf-event-data-files.yml) as a template, create a deployment action for your dataset.
