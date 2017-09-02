#!/usr/bin/env python
import boto3
name=raw_input("Location of the file to be uploaded:")
s3res=boto3.resource('s3')
buckets=s3res.buckets.all()
for bucket in buckets:
	print bucket.name
bucketname=raw_input("Please the enter the bucket name you want to upload to:")
newfilename=raw_input("Please enter the new file name you want to save it as:")
s3client=boto3.client('s3')
s3client.upload_file(name,bucketname,newfilename)
for bucket in buckets:
	for obj in bucket.objects.all():
		print obj

