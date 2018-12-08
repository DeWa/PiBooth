from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.loader import Loader
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.animation import Animation
from kivy.uix.camera import Camera
from library.progress import ProgressSpinner
from library.imageutil import PhotoThread, convert_photo

import os
import time
import threading

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

Builder.load_file(os.path.join(__location__, 'photo.kv'))


class PhotoScreen(Screen):
    buttonLabel = "Start countdown"
    flash_opacity = NumericProperty(0)
    flash_animation = Animation(flash_opacity=0)

    def on_enter(self):
        self.countdown = 5
        self.buttonLabel = "Start countdown"
        self.ids.countdown_button.text = "Start countdown"
        self.timerStart = 0
        self.timerStarted = False
        self.countdown_started = False

        self.app = App.get_running_app()
        self.camera = self.app.camera
        self.camera.play = True

        # Add widgets
        self.ids["camera_wrapper"].add_widget(self.camera, 3)
        self.ids["camera_wrapper"].remove_widget(self.ids["loading_spinner"])
        self.ids["frame"].opacity = 1
        self.ids["countdown_button"].opacity = 1

        self.update_frame()

    def countdown_func(self, dt):
        self.countdown -= 1
        if self.countdown <= 0:
            Clock.unschedule(self.countdown_interval)
            self.take_photo()

        self.ids.countdown_button.text = str(self.countdown)

    def start_countdown(self):
        if self.countdown_started is not True:
            self.countdown_started = True
            self.countdown_interval = Clock.schedule_interval(
                self.countdown_func, 1.0)

    def take_photo(self):
        # Remove photo related widgets
        self.camera.play = False
        self.ids["camera_wrapper"].remove_widget(self.camera)
        self.ids["frame"].opacity = 0
        self.ids["countdown_button"].opacity = 0

        # Save Photo
        timestr = time.strftime("%Y%m%d_%H%M%S")
        path = "./photos/original/{}".format(timestr)
        self.camera.take_picture(path)
        self.app.state['currentPhoto'] = timestr

        # Add loading spinner
        self.flash_opacity = 1
        self.ids["camera_wrapper"].add_widget(self.ids["loading_spinner"], 3)
        self.flash_animation.start(self)

        # Convert photo
        convert_thread = PhotoThread(
            name='convert_thread',
            target=convert_photo,
            callback=self.next_screen,
            callback_args=("hello", "world"),
            args=(timestr, self.get_frame_source(),)
        )
        convert_thread.start()
    
    def wait_animation(self):
        self.flash_animation.bind(on_complete=self.next_screen)

    def next_screen(self, *args, **kwargs):
        self.manager.current = 'preview'

    def get_frame_source(self):
        return self.app.frames[self.app.state['frame']]

    def update_frame(self):
        self.ids.frame.source = self.get_frame_source()

    def on_pre_leave(self):
        self.ids["camera_wrapper"].remove_widget(self.camera)