#!/usr/bin/env python
import boto3
ec2_conn=boto3.resource('ec2')
instances=ec2_conn.instances.filter(Filters=[{'Name':'instance-state-name','Values':['running']}])
ids=[]
for instance in instances:
	ids.append(instance.id)
	print instance.id, instance.instance_type
ec2_conn.instances.filter(InstanceIds=ids).terminate()
