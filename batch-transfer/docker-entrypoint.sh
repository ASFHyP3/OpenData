#!/bin/bash

set -ex

src_bucket="$1"
dst_bucket="$2"
s3_prefix="$3"

aws s3 sync --only-show-errors "s3://$src_bucket/$s3_prefix" "s3://$dst_bucket/$s3_prefix"
