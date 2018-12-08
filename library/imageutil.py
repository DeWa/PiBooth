import PIL
import threading
from PIL import Image
from .config import config

__all__ = ['convert_photo']

def add_frames(img, framesrc):
    frames = Image.open(framesrc).convert('RGBA').resize(img.size)
    new_image = Image.alpha_composite(img, frames)

    return new_image

def make_resizes(img, name):
    screen_width = 600
    thumbnail_width = 120

    # TODO: DRY... I know...
    wpercent = (screen_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    
    img = img.resize((screen_width, hsize), PIL.Image.ANTIALIAS)
    img.save("%s/screen/%s.png" % (config["photo_path"], name))

    wpercent = (thumbnail_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    
    img = img.resize((thumbnail_width, hsize), PIL.Image.ANTIALIAS)
    img.save("%s/thumbnails/%s.png" % (config["photo_path"], name))
    

def convert_photo(photo_name, frame_source):    
    img = Image.open("%s/original/%s.jpg" % (config["photo_path"], photo_name)).convert('RGBA')
    
    # Add frames
    framedImages = add_frames(img, frame_source)
    framedImages.save("%s/final/%s.png" % (config["photo_path"], photo_name))

    # Resize
    make_resizes(framedImages, photo_name, )

class PhotoThread(threading.Thread):
    def __init__(self, callback=None, callback_args=None, *args, **kwargs):
        target = kwargs.pop('target')

        super(PhotoThread, self).__init__(target=self.target_with_callback, *args, **kwargs)
        self.callback = callback
        self.method = target
        self.callback_args = callback_args

    def target_with_callback(self, photo_name, frame_source):
        self.method(photo_name, frame_source)
        if self.callback is not None:
            self.callback(*self.callback_args)