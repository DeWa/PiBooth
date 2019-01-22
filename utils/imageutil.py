import PIL
import threading
import time
from PIL import Image
from .config import config

def add_frames(img, framesrc):
    frames = Image.open(framesrc).resize(img.size)
    new_image = Image.alpha_composite(img, frames)
    return new_image

def make_preview(photo_name, frame_source):
    img = Image.open("%s/original/%s.jpg" % (config["photo_path"], photo_name)).convert('RGBA')

    wpercent = (config["screen_size"] / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    smallimg = resize_photo(img, (config["screen_size"], hsize))

    framedImages = add_frames(smallimg, frame_source)
    framedImages.save("%s/screen/%s.png" % (config["photo_path"], photo_name))

def resize_photo(image, size):
    resized_image = image.resize((size[0], size[1]), PIL.Image.ANTIALIAS)
    return resized_image

def make_final(photo_name, frame_source):
    img = Image.open("%s/original/%s.jpg" % (config["photo_path"], photo_name)).convert('RGBA')
    framedImages = add_frames(img, frame_source)
    framedImages.save("%s/final/%s.png" % (config["photo_path"], photo_name), format='JPEG')
    

class PreviewThread(threading.Thread):
    def __init__(self, callback=None, callback_args=None, *args, **kwargs):
        target = kwargs.pop('target')

        super(PreviewThread, self).__init__(target=self.target_with_callback, *args, **kwargs)
        self.callback = callback
        self.method = target
        self.callback_args = callback_args

    def target_with_callback(self, photo_name, frame_source):
        self.method(photo_name, frame_source)
        if self.callback is not None:
            self.callback()
