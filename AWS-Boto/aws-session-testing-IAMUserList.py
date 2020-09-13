import boto3

#Connection syntax.
AWS_CONNECTION=boto3.session.Session()
'''
This is another way of creating session using a profile.
AWS_CONN=boto3.session.Session(profile_name="pbangari")
'''
IAM_CONSOLE=AWS_CONNECTION.resource('iam')

'''
IAM_CONN=boto3.resource("iam")
'''
for each_user in IAM_CONSOLE.users.all():
    print(each_user.name)
