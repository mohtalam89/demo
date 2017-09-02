#!/usr/bin/env python
import boto3
s3res=boto3.resource('s3')
buckets=s3res.buckets.all()
for bucket in buckets:
	for obj in bucket.objects.all():
		print obj
