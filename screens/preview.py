from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
import time


import os
import time

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

Builder.load_file(os.path.join(__location__, 'preview.kv'))


class PreviewScreen(Screen):
    def on_enter(self):
        self.app = App.get_running_app()
        self.ids.photo.source = "./photos/screen/%s.png" % self.app.state['currentPhoto']
