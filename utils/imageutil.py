import PIL
import threading
import time
from PIL import Image
from utils.httputils import send_image_to_api
from utils.state import State


def add_frames(img, framesrc):
    frames = Image.open(framesrc).resize(img.size)
    new_image = Image.alpha_composite(img, frames)
    return new_image


def make_preview(photo_name, frame_source):
    image_path = State.get("photopath")
    image_width = State.get("preview_image_width")

    img = Image.open("%s/original/%s.jpg" %
                     (image_path, photo_name)).convert('RGBA')

    wpercent = (int(image_width) / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    smallimg = resize_photo(img, (int(image_width), hsize))

    framedImages = add_frames(smallimg, frame_source)
    framedImages.save("%s/screen/%s.png" % (image_path, photo_name))


def resize_photo(image, size):
    resized_image = image.resize((size[0], size[1]), PIL.Image.ANTIALIAS)
    return resized_image


def make_final(photo_name, frame_source):
    image_path = State.get("photopath")
    img = Image.open("%s/original/%s.jpg" %
                     (image_path, photo_name)).convert('RGBA')
    framedImages = add_frames(img, frame_source)
    framedImages.save("%s/final/%s.png" % (image_path, photo_name))


class PreviewThread(threading.Thread):
    def __init__(self, callback=None, callback_args=None, *args, **kwargs):
        target = kwargs.pop('target')

        super(PreviewThread, self).__init__(
            target=self.target_with_callback, *args, **kwargs)
        self.callback = callback
        self.method = target
        self.callback_args = callback_args

    def target_with_callback(self, photo_name, frame_source):
        self.method(photo_name, frame_source)
        if self.callback is not None:
            self.callback()


class CreateFinalAndSendThread(threading.Thread):
    def __init__(self, threadID, name, photo_name, frame_source):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.photo_name = photo_name
        self.frame_source = frame_source
        photo_path = State.get("photopath")
        self.image_path = "%s/final/%s.png" % (photo_path, photo_name)
        self.sharecode = State.get('share_code')

    def run(self):
        print("Starting thread %s and creating final photo for %s" %
              (self.name, self.photo_name))
        make_final(self.photo_name, self.frame_source)

        print("Photo created! Sending to API")
        send_image_to_api(
            self.image_path, self.photo_name + ".png", self.sharecode)
        print("Exiting " + self.name)
