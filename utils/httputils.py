import random
import requests
import boto3
from utils.state import State
from requests.adapters import HTTPAdapter

s = requests.Session()
s.mount('http', HTTPAdapter(max_retries=3))
s.mount('https', HTTPAdapter(max_retries=3))

s3 = boto3.client('s3')

def create_share_code():
    chars = '0123456789ABCDEF'
    return ''.join(random.choice(chars) for i in range(5))


def send_image_to_api(image_path, image_name, sharecode):
    upload_url = State.get("upload_url")
    headers = {'Authorization': State.get('api_key')}
    
    # Create placeholder image
    sharecode_response = requests.post(
        upload_url, data={'code': sharecode}, headers=headers)

    files = {'image': (image_name, open(image_path, 'rb'), 'image/png')}
    response = requests.post("%s/%s" % (upload_url, sharecode), headers=headers, files=files)

def send_image_to_s3(image_path, sharecode):
  bucket_name = State.get("s3_bucket_name")
  s3.upload_file(image_path, bucket_name, sharecode + '.jpg')
  