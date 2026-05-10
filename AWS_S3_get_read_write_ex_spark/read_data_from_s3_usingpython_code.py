import boto3
import csv
s3 = boto3.client("s3")
response = s3.get_object(Bucket='venky-de-bucket', Key='user1.csv')
csv_content = response["Body"].read().decode("utf-8")
print(csv_content)

#This will print all file names inside the bucket.
response1 = s3.list_objects_v2(Bucket='venky-de-bucket')

for obj in response1['Contents']:
    print(obj['Key'])

