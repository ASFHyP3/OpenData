#!/bin/bash

set -ex

aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin $1.dkr.ecr.us-west-2.amazonaws.com
docker build -t opendata-transfer .
docker tag opendata-transfer:latest $1.dkr.ecr.us-west-2.amazonaws.com/opendata-transfer:latest
docker push $1.dkr.ecr.us-west-2.amazonaws.com/opendata-transfer:latest
