profile ?= tools-sandbox

image_uri ?= '050846374571.dkr.ecr.us-west-2.amazonaws.com/opendata-transfer:latest'  # Tools Sandbox
vpc_id ?= None
subnet_ids ?= None
stack_name ?= opendata-transfer
deploy:
	aws --profile $(profile) cloudformation deploy \
		--template-file batch-cf.yml \
		--stack-name=$(stack_name) \
		--capabilities CAPABILITY_IAM \
		--parameter-overrides \
		  ImageUri=$(image_uri) \
		  VpcId=$(vpc_id) \
		  SubnetIds=$(subnet_ids)

aws_account ?= 050846374571  # Tools Sandbox
docker:
	AWS_PROFILE=$(profile) ./docker-build.sh $(aws_account)

s3_prefix ?= foo
job_name ?= foo
submit-job:
	aws --profile $(profile) batch submit-job --job-name $(job_name) --job-queue opendata-transfer-job-queue --job-definition opendata-transfer-job-definition --parameters "s3_prefix=$(s3_prefix)"
