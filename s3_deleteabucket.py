#!/usr/bin/env python
import boto3
print "Deleting a Bucket from Your AWS Infrastructure"
s3res=boto3.resource('s3')
buckets=s3res.buckets.all()
print "Please choose the appropriate bucket"
for bucket in buckets:
	print bucket.name
bucketname=raw_input('Please enter the bucket you want to delete:')
buckets=s3res.buckets.all()
if bucket.name == bucketname:
	for obj in bucket.objects.all():
		obj.delete()
	bucket.delete()
print "check whether the bucket you have entered is deleted or not"
for bucket in buckets:
	print bucket.name

