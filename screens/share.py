from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty

from components.qrcode import QRCodeWidget
from utils.state import State
from utils.httputils import create_share_code

import os
import time

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

Builder.load_file(os.path.join(__location__, 'share.kv'))


class ShareScreen(Screen):
    imageurl = StringProperty("")
    sharecode = StringProperty("")

    def __init__(self, **kwargs):
        super(ShareScreen, self).__init__(**kwargs)

    def on_enter(self):
        self.app = App.get_running_app()
        self.sharecode = create_share_code()
        self.imageurl = '%s%s' % (State.get('photo_url'), self.sharecode)
        self.reset_timer = Clock.schedule_interval(
            self.reset_app, State.get('reset_time'))

    def reset_app(self, dt):
        self.manager.current = 'start'
