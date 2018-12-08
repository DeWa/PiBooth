#from lib.vendor.camerabase import Camera
from lib.vendor.camerauix import Camera

from pprint import pprint
pprint(vars(Camera))


class BoothCamera(Camera):
    def __init__(self):
        super().__init__(id="camera", resolution=(1280, 720), size=(800, 600), play=True)

    def take_picture(self, path):
        self._camera.take_picture(path)
