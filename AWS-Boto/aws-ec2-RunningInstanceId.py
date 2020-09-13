# This script takes the hostname as input from jumpstation and returns the health status.
import boto3
from sys import *

# Check if the script is executed with one parameter as input.
if len(argv) != 2:
    print("This script takes an input of a valid hostname. \nExecute the script with hostname as parameter. \nExample:\n ./aws-host-health-check.py hostname")
    exit()

input_hostname=argv[1]
input_hostname_split=input_hostname.split('.')

# Validating the hostname with some basic checks and identifying the datacenter of the host.
if len(input_hostname_split) == 6 and input_hostname_split[-2] == 'drcloud' and input_hostname_split[-1] == 'zone':
    DATA_CENTER=input_hostname_split[3]
    if DATA_CENTER == 'vdc7':
        AWS_REGION_NAME = 'eu-west-1'
    elif DATA_CENTER == 'vdc3':
        AWS_REGION_NAME = 'us-east-1'
    elif DATA_CENTER == 'vdc2':
        AWS_REGION_NAME = 'us-west-2'
    else:
        print("The entered hostname do not qualify the hostname standards.\nExample:\nh010072064133.gc-app-prd.aws-ew1-b.vdc7.drcloud.zone")
        exit()
else:
    print("The entered hostname do not qualify the hostname standards.\nExample:\nh010072064133.gc-app-prd.aws-ew1-b.vdc7.drcloud.zone")
    exit()

# AWS Console connection using the default session users registered for your aws-cli
AWS_EC2_CONSOLE_CLIENT = boto3.client(service_name="ec2",region_name=AWS_REGION_NAME)

# Deriving the instance_id of the inputed hostname using filters
f_instance_hostname={"Name": "tag:hostname", "Values":[input_hostname]}
input_instance_id=AWS_EC2_CONSOLE_CLIENT.describe_instances(Filters=[f_instance_hostname])['Reservations']
for each_instances in input_instance_id:
    for each in each_instances['Instances']:
        instance_id=each['InstanceId']
        print(f"Instance State: {each['State']['Name']}")

AWS_EC2_INSTANCE_STATUS = AWS_EC2_CONSOLE_CLIENT.describe_instance_status(InstanceIds=[instance_id])
for each_ec2_item in AWS_EC2_INSTANCE_STATUS['InstanceStatuses']:
    for each_ec2_item_status in each_ec2_item['SystemStatus']['Details']:
        print(f"Host: {input_hostname} health check is {each_ec2_item_status['Status']}")
