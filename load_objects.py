import boto3

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)

# Загрузить объекты в бакет

## Из строки
s3.put_object(Bucket='bucket-elisseeff', Key='README_01', Body='TEST', StorageClass='COLD')

print('s3.put_object')
input()

## Из файла
s3.upload_file('README.md', 'bucket-elisseeff', 'README.md')
s3.upload_file('load_objects.py', 'bucket-elisseeff', 'load_objects.py')