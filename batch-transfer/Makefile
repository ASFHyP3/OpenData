cf_bucket ?= 'cf-templates-1hz9ldhhl4ahu-us-west-2'  # Tools Sandbox
VpcId ?= None
SubnetIds ?= None
deploy:
	aws cloudformation package \
		--template-file batch-cf.yml \
		--s3-bucket=$(cf_bucket) \
		--output-template-file packaged.yml && \
	aws cloudformation deploy \
		--template-file packaged.yml \
		--stack-name='opendata-transfer' \
		--capabilities CAPABILITY_IAM \
		--parameter-overrides \
		  VpcId=$(vpc_id) \
		  SubnetIds=$(subnet_ids)
