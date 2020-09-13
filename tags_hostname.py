import boto3
AWS_EC2_CONSOLE_CLIENT = boto3.client(service_name="ec2",region_name="eu-west-1")

tag_instance_hostname={"Name": "tag:hostname", "Values":['h010072064133.gc-app-prd.aws-ew1-b.vdc7.drcloud.zone']}
input_instance_id=AWS_EC2_CONSOLE_CLIENT.describe_instances(Filters=[tag_instance_hostname])['Reservations']

#for each_instances in input_instance_id["Instances"]:
#    print(each_instances["InstanceId"])
for each_instances in input_instance_id:
    print(each_instances)
    for each in each_instances['Instances']:
        print(each['InstanceId'])
