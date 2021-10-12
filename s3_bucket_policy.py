'''
Report bucket policy
'''
import boto3

client = boto3.client('s3')
s3 = boto3.resource('s3')

response = client.list_buckets()

for bucket_name in response['Buckets']:
    try:
        bucket_policy = s3.BucketPolicy(bucket_name['Name'])
        print(f"\n{bucket_name['Name']}\n{bucket_policy.policy}")
    except:
        print(f"\n{bucket_name['Name']}\nNo policy defined")
