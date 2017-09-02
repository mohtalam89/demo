#!/usr/bin/env python
import boto3
s3res=boto3.resource('s3')
buckets=s3res.buckets.all()
print 'Please locate the object to be deleted '
for bucket in buckets:
	for obj in bucket.objects.all():
		print obj

s3client=boto3.client('s3')
bucket=raw_input("Please enter the bucket name:")
file=raw_input("Please enter the object name:")
s3client.delete_object(Bucket=bucket,Key=file)
print 'check if the object %s has been deleted from the bucket %s' %(file,bucket)
for bucket in buckets:
	for obj in bucket.objects.all():
		print obj
