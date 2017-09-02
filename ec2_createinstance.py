#!/usr/bin/env python
import boto3
ec2_conn=boto3.resource('ec2')
imageid=raw_input("Please enter your ImageId(ami-08111162):")
keyname=raw_input("Please enter the aws key(awskey):")
instancetype=raw_input("Please enter the instance type(t2.micro):")
subnetid=raw_input("Please enter the subnet id(subnet-3f696a67):")
instance=ec2_conn.create_instances(ImageId=imageid,MinCount=1,MaxCount=1,KeyName=keyname,InstanceType=instancetype,SubnetId=subnetid)
print "Ec2 Instance Created as:"
print instance
