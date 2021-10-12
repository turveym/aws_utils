'''
Report encryption status of buckets
'''
import boto3

client = boto3.client('s3')

response = client.list_buckets()

for bucket_name in response['Buckets']:
    try:
        encryption_state = client.get_bucket_encryption(Bucket=bucket_name['Name'])
        print(f"{bucket_name['Name']} encryption: {encryption_state['ServerSideEncryptionConfiguration']['Rules'][0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']}")
    except:
        print(f"{bucket_name['Name']} not encrypted")
