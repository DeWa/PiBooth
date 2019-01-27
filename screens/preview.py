from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from utils.httputils import create_share_code
from utils.imageutil import CreateFinalAndSendThread

from utils.state import State

import time


import os
import time

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

Builder.load_file(os.path.join(__location__, 'preview.kv'))


class PreviewScreen(Screen):
    def on_enter(self):
        self.app = App.get_running_app()
        self.ids.photo.source = "%s/screen/%s.png" % (
            State.get('photopath'), State.get('currentPhoto'))

    def on_confirm(self):
        sharecode = create_share_code()
        State.set(('share_code', sharecode))

        current_photo = State.get('currentPhoto')

        photo_thread = CreateFinalAndSendThread(
            1, "Thread-1", current_photo, self.get_frame_source())
        photo_thread.start()
        self.manager.current = 'share'

    def get_frame_source(self):
        frames = State.get('lowres_frames')
        return frames[State.get('frame')]
