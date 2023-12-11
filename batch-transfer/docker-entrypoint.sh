#!/bin/bash

set -ex

aws s3 sync --only-show-errors "s3://its-live-data/$1" "s3://its-live-open/$1"
