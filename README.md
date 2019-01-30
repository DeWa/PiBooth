# PiBooth
PiBooth is Python-based Photobooth app for Raspberry Pi. It uses Kivy for rendering and is designed to for the official Raspberry Pi Touchscreen and Camera.

## Installation

### Kivy
Install dependencies
```
sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
   pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   python-setuptools libgstreamer1.0-dev git-core \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} python-dev libmtdev-dev \
   xclip xsel
```
Install newer version of Cython
```
sudo pip install -U Cython==0.28.2
```
Install Kivy globally
```
sudo pip install git+https://github.com/kivy/kivy.git@master
```

### Raspberry Pi

Change Raspbi touchscreen to default touch method by editing kivy's configs with ``vim ~/.kivy/config.ini``
```
mouse = mouse
mtdev_%(name)s = probesysfs,provider=mtdev
hid_%(name)s = probesysfs,provider=hidinput
```

Install Raspberry Pi Camera dependencies
```
sudo apt-get install python-gst0.10 gstreamer0.10-plugins-good gstreamer0.10-plugins-ugly
```

You also need 'Fredoka' font which can be found from [Google fonts](https://fonts.google.com/specimen/Fredoka+One). 

## Usage

1. Change configs if needed at ``photobooth.ini``
2. Add Frames

   Add two set of frames: highres (resolution 3280x2464) and lowres (resolution 640x480).
   Lowres frames are used in the livevideo and previews whereas highres are used when creating the final photos.
   Copy highres frames to  ``./assets/frames`` folder and lowres counterparts (with the same name) to ``./assets/frames/lowres`` 

3. Start UI
   ```
   python3 main.py
   ```

4. Start UI at the startup
   
   ***TODO***

## Troubleshooting
  - *Photobooth gives me ``Segmentation fault`` at the startup*

You have probably imported the libraries at the wrong order in main.py. The right order is
```
import os, glob
os.environ['KIVY_GL_BACKEND'] = 'gl'
import kivy
```
This will be fixed in the future.

## License
MIT


