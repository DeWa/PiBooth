# For some reason Kivy uses wrong GL_BACKEND in the Raspberry Pi
# This is here to fix it and this must be imported in this order
# TODO: Change this to .env or .ini setting later
import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
import kivy

from screens.share import ShareScreen
from screens.preview import PreviewScreen
from screens.start import StartScreen
from screens.photo import PhotoScreen
from lib.boothcamera import BoothCamera
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder
from kivy.app import App



Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')
kivy.require('1.0.7')


class Photobooth(App):
    state = {
        "frame": 0,
        "photopath": "/",
        "currentPhoto": "20181202_132921"
    }

    frames = [
        "./assets/frames/frame1.png",
        "./assets/frames/frame2.png"
    ]

    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(PhotoScreen(name='photo'))
        sm.add_widget(PreviewScreen(name='preview'))
        sm.add_widget(ShareScreen(name='share'))
        return sm


if __name__ == '__main__':
    Photobooth().run()
