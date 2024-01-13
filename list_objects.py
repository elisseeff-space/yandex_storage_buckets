import boto3

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)

response = s3.list_buckets()
buckets = response['Buckets']
print('Buckets:')
for bucket in buckets:
    print(f"\t{bucket['Name']}")
    if bucket['Name'] != 'www.elisseeff.site' :
        for key in s3.list_objects(Bucket=bucket['Name'])['Contents']:
            print(f"{key['Key']}\n")

# Получить список объектов в бакете
#for key in s3.list_objects(Bucket='bucket-elisseeff')['Contents']:
#    print(f"{key['Key']}\n")
            
# List objects in an Amazon S3 bucket
s3 = boto3.resource('s3')
bucket = s3.Bucket('new-bucket-elis')
for obj in bucket.objects.all():
    print(obj.key)

# List top-level common prefixes in Amazon S3 bucket
client = boto3.client('s3')
paginator = client.get_paginator('list_objects')
result = paginator.paginate(Bucket='new-bucket-elis', Delimiter='/')
for prefix in result.search('CommonPrefixes'):
    print(prefix.get('Prefix'))
