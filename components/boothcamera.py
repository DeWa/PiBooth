from vendor.camerauix import Camera

class BoothCamera(Camera):
    def __init__(self):
        super().__init__(id="camera", resolution=(640, 480), size=(800, 600), play=True)

    def take_picture(self, path):
        self._camera.take_picture(path)
