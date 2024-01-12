import boto3, io, PIL
from PIL import Image
from io import BytesIO


session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)

# Получить объект
get_object_response = s3.get_object(Bucket='elisseeffdata',Key='test_catalog/loewe_1.jpg')
#print(get_object_response['Body'].read())
#print(get_object_response)

image = Image.open(io.BytesIO(get_object_response['Body'].read()))
#image.show()
PIL.ImageShow.show(image)