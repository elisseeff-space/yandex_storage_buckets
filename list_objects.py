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
