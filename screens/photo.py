from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.loader import Loader
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.animation import Animation
from kivy.uix.camera import Camera
from components.progress import ProgressSpinner
from utils.imageutil import PreviewThread, make_preview

import os
import time
import threading


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

Builder.load_file(os.path.join(__location__, 'photo.kv'))


class PhotoScreen(Screen):
    flash_opacity = NumericProperty(0)
    flash_animation = Animation(flash_opacity=0)
    countdown = NumericProperty(0)

    def on_enter(self):
        self.countdown = 5
        self.timerStart = 0
        self.timerStarted = False
        self.countdown_started = False

        self.app = App.get_running_app()
        self.camera = self.app.camera
        self.camera.size_hint = (1, 1)
        self.camera.play = True

        # Add widgets
        self.ids["camera_wrapper"].add_widget(self.camera, 4)
        self.ids["camera_wrapper"].remove_widget(self.ids["loading_spinner"])
        self.ids["frame"].opacity = 1
        self.ids["countdown_button"].opacity = 1
        self.ids["back_button"].opacity = 1
        self.ids["countdown_label"].opacity = 0

        self.ids["countdown_button"].disabled = False
        self.ids["back_button"].disabled = False

        self.update_frame()

    def countdown_func(self, dt):
        self.countdown -= 1
        if self.countdown <= 0:
            Clock.unschedule(self.countdown_interval)
            self.take_photo()

    def start_countdown(self):
        if self.countdown_started is not True:
            self.countdown_started = True
            self.countdown_interval = Clock.schedule_interval(
                self.countdown_func, 1.0)

        self.ids["countdown_label"].opacity = 1
        # Hide buttons
        self.ids["countdown_button"].opacity = 0
        self.ids["back_button"].opacity = 0
        self.ids["countdown_button"].disabled = True
        self.ids["back_button"].disabled = True

    def take_photo(self):
        # Remove photo related widgets
        self.camera.play = False
        self.ids["camera_wrapper"].remove_widget(self.camera)
        self.ids["frame"].opacity = 0
        self.ids["countdown_label"].opacity = 0
        self.ids["countdown_button"].opacity = 0
        self.ids["back_button"].opacity = 0

        # Save Photo
        timestr = time.strftime("%Y%m%d_%H%M%S")
        path = "./photos/original/{}".format(timestr)
        self.camera.take_picture(path)
        self.app.state['currentPhoto'] = timestr

        # Add loading spinner
        self.flash_opacity = 1
        self.ids["camera_wrapper"].add_widget(self.ids["loading_spinner"], 4)
        self.flash_animation.start(self)

        # Make preview
        preview_thread = PreviewThread(
            name='preview_thread',
            target=make_preview,
            callback=self.next_screen,
            args=(timestr, self.get_frame_source(),)
        )
        preview_thread.start()

    def next_screen(self):
        self.manager.current = 'preview'

    def get_frame_source(self):
        return self.app.frames[self.app.state['frame']]

    def update_frame(self):
        self.ids.frame.source = self.get_frame_source()

    def on_pre_leave(self):
        self.ids["camera_wrapper"].remove_widget(self.camera)
