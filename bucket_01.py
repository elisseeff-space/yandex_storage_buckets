import boto3

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)

# Создать новый бакет
try:
    s3.create_bucket(Bucket='bucket-elisseeff_01')
except Exception as e:
    print(f'Exception {e}') 

# Загрузить объекты в бакет

## Из строки
s3.put_object(Bucket='bucket-elisseeff_01', Key='object_elisseef_01', Body='TEST', StorageClass='COLD')

print('s3.put_object')
input()

## Из файла
s3.upload_file('README.md', 'bucket-elisseeff_01', 'README.md')
s3.upload_file('README.md', 'bucket-elisseeff_01', 'README/README.md')

print('s3.upload_file')
input()

# Получить список объектов в бакете
for key in s3.list_objects(Bucket='bucket-elisseeff_01')['Contents']:
    print(key['Key'])

print('список объектов в бакете')
input()

# Удалить несколько объектов
#forDeletion = [{'Key':'object_elisseeff'}, {'Key':'script/py_script.py'}]
#response = s3.delete_objects(Bucket='bucket-elisseeff', Delete={'Objects': forDeletion})

# Получить объект
get_object_response = s3.get_object(Bucket='bucket-elisseeff',Key='py_script.py')
print(get_object_response['Body'].read())
