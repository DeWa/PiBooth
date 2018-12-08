from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.loader import Loader
from kivy.uix.camera import Camera
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

Builder.load_file(os.path.join(__location__, 'start.kv'))


class StartScreen(Screen):
    def on_enter(self):
        self.a = App.get_running_app()
        self.camera = self.a.camera
        self.camera.play = True
        self.ids["camera_wrapper"].add_widget(self.camera)
        self.update_frame()

    def next_frame(self):
        frame_number = self.a.state['frame']
        next_frame = frame_number + 1

        if next_frame > len(self.a.frames) - 1:
            self.a.state['frame'] = 0
        else:
            self.a.state['frame'] = next_frame

        self.update_frame()

    def prev_frame(self):
        frame_number = self.a.state['frame']
        next_frame = frame_number - 1

        if next_frame < 0:
            self.a.state['frame'] = len(self.a.frames) - 1
        else:
            self.a.state['frame'] = next_frame

        self.update_frame()

    def get_frame_source(self):
        return self.a.frames[self.a.state['frame']]

    def update_frame(self):
        self.ids.frame.source = self.get_frame_source()

    def on_pre_leave(self):
        self.ids["camera_wrapper"].remove_widget(self.camera)
