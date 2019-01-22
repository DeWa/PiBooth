from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty
from components.qrcode import QRCodeWidget



import os
import time

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

Builder.load_file(os.path.join(__location__, 'share.kv'))


class ShareScreen(Screen):
    imageurl = StringProperty("")

    def __init__(self, **kwargs):
        super(ShareScreen, self).__init__(**kwargs)

    def on_enter(self):
        self.app = App.get_running_app()
        print(self.app.config)
        self.reset_timer = Clock.schedule_interval(
                self.reset_app, 20)
    
    def reset_app(self, dt):
        self.manager.current = 'start'
