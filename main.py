# For some reason Kivy uses wrong GL_BACKEND in the Raspberry Pi
# This is here to fix it and this must be imported in this order
# TODO: Change this to .env or .ini setting later
import os, glob
os.environ['KIVY_GL_BACKEND'] = 'gl'
import kivy

from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition 
from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder
from kivy.app import App
from kivy.config import ConfigParser

from screens.share import ShareScreen
from screens.preview import PreviewScreen
from screens.start import StartScreen
from screens.photo import PhotoScreen
from components.boothcamera import BoothCamera
from utils.state import State

kivy.require('1.0.7')
kivy.cache.Cache._categories['kv.texture']['limit'] = 50

class Photobooth(App):
    def build(self):
        self.init_frames()
        Builder.load_string('''
<Photobooth>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        ''')
        self.camera = BoothCamera()
        sm = ScreenManager(transition=SwapTransition())
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(PhotoScreen(name='photo'))
        sm.add_widget(PreviewScreen(name='preview'))
        sm.add_widget(ShareScreen(name='share'))
        return sm

    def build_config(self, config):
        config.setdefaults("photobooth", {
            "photopath": "/photos",
            "preview_image_width": 600,
            "photo_countdown": 5,
            "reset_time": 20,
            "upload_url": "https://dont.use.change/me",
            "photo_url": "https://get.photo.here/"
        })
        config.read('photobooth.ini')
        State.set_dict({
            "lowres_frames": None,
            "highres_frames": None,
            "photopath": config.get('photobooth', 'photopath'),
            "frame": 0,
            "current_photo": None,
            "share_code": "",
            "preview_image_width": config.get('photobooth', 'preview_image_width'),
            "photo_countdown": config.get('photobooth', 'photo_countdown'),
            "reset_time": float(config.get('photobooth', 'reset_time')),
            "upload_url": config.get('photobooth', 'upload_url'),
            "photo_url": config.get('photobooth', 'photo_url'),
            "api_key": config.get('photobooth', 'api_key')
        })

    def init_frames(self):
        highres_frames = glob.glob("%s/assets/frames/*.png" % os.getcwd())
        lowres_frames = glob.glob("%s/assets/frames/lowres/*.png" % os.getcwd())
        
        if len(highres_frames) == 0:
            raise OSError('No frames found!')
        elif len(lowres_frames) == 0:
            raise OSError('Lowres frames are missing!')
        elif len(highres_frames) != len(lowres_frames):
            raise OSError('Lowres and Highres frames are not matching!')
        State.set_dict({
            "lowres_frames": lowres_frames,
            "highres_frames": highres_frames,
        })

if __name__ == '__main__':
    State.init()
    Photobooth().run()
