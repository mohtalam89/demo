#!/usr/bin/env python
import boto3
s3client=boto3.client('s3')
bucketname=raw_input("Please enter a AWS Bucket name to creat:")
s3client.create_bucket(Bucket=bucketname)
