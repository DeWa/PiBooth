from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.loader import Loader
from kivy.clock import Clock

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

    def countdown_func(self, dt):
        print(self.countdown)
        self.countdown -= 1
        self.ids.countdown_button.text = str(self.countdown)

    def start_countdown(self):
        Clock.schedule_interval(self.countdown_func, 1.0)
