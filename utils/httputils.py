import random
import requests
from utils.state import State


def create_share_code():
    chars = '0123456789ABCDEF'
    return ''.join(random.choice(chars) for i in range(5))


def send_image_to_api(image_path, image_name, sharecode):
    upload_url = State.get("upload_url")
    # Create placeholder image
    sharecode_response = requests.post(upload_url, data={'code': sharecode})

    if sharecode_response.status_code == 200:
        files = {'image': (image_name, open(image_path, 'rb'), 'image/png')}
        response = requests.post(
            "%s/%s" % (upload_url, sharecode), files=files)

        if response.status_code != 200:
            print("Error while uploading a photo")
    else:
        print("Error while creating placeholder photo")
