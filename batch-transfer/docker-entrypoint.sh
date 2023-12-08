#!/bin/bash

set -ex

aws s3 sync --no-progress "s3://its-live-data/$1" "s3://its-live-open/$1"
