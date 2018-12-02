import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from screens.photo import PhotoScreen
from screens.start import StartScreen
from screens.preview import PreviewScreen

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
        "./assets/frame1.png",
        "./assets/frame2.png"
    ]

    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(PhotoScreen(name='photo'))
        sm.add_widget(PreviewScreen(name='preview'))
        return sm


if __name__ == '__main__':
    Photobooth().run()
