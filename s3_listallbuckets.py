#!/usr/bin/env python
import boto3
s3res=boto3.resource('s3')
buckets=s3res.buckets.all()
for bucket in buckets:
	print bucket.name
