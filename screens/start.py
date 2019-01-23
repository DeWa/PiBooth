from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.loader import Loader
from kivy.uix.camera import Camera
import os

from utils.state import State

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

Builder.load_file(os.path.join(__location__, 'start.kv'))


class StartScreen(Screen):
    def on_enter(self):
        State.print()
        self.a = App.get_running_app()
        self.camera = self.a.camera
        self.camera.play = True
        self.ids["camera_wrapper"].add_widget(self.camera, 2)
        self.frames = State.get('lowres_frames')
        self.update_frame()

    def next_frame(self):
        frame_number = int(State.get('frame'))
        next_frame_number = frame_number + 1

        if next_frame_number > len(self.frames) - 1:
             State.set(('frame', 0))
        else:
            State.set(('frame', next_frame_number))

        self.update_frame()

    def prev_frame(self):
        frame_number = State.get('frame')
        next_frame_number = frame_number - 1

        if next_frame_number < 0:
            State.set(('frame', len(self.frames) - 1))
            State.print()
        else:
            State.set(('frame', next_frame_number))

        self.update_frame()

    def get_frame_source(self):
        return self.frames[State.get('frame')]

    def update_frame(self):
        self.ids.frame.source = self.get_frame_source()

    def on_pre_leave(self):
        self.ids["camera_wrapper"].remove_widget(self.camera)
