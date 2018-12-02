from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.loader import Loader
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.animation import Animation


import os
import time

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

Builder.load_file(os.path.join(__location__, 'photo.kv'))


class PhotoScreen(Screen):
    countdown = 5
    buttonLabel = "Start countdown"
    timerStart = 0
    timerStarted = False
    flash_opacity = NumericProperty(0)
    countdown_started = False
    flash_animation = Animation(flash_opacity=0)

    def on_enter(self):
        self.flash_animation.bind(on_complete=self.next_screen)

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
        camera = self.ids['camera']

        camera.play = False
        timestr = time.strftime("%Y%m%d_%H%M%S")
        # Change this to Raspberry Pi's own camera capture when used in that
        camera.export_to_png("./photos/IMG_{}.png".format(timestr))

        self.flash_opacity = 1
        self.flash_animation.start(self)

    def next_screen(self, *args):
        self.manager.current = 'preview'
