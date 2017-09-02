#!/usr/bin/env python
import boto3
import os
ec2_conn=boto3.resource('ec2')
instances=ec2_conn.instances.filter(Filters=[{'Name':'instance-state-name','Values':['running']}])
ids=[]
for instance in instances:
	ids.append(instance.id)
	print instance.id, instance.instance_type,instance.launch_time,instance.state['Name'],instance.public_ip_address
if len(ids) == 0:
	os.system('clear')
	print "No Ec2 instances seen"
