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

## Usage

Change configs if needed at ``photobooth.ini``

Start UI
```
python3 main.py
```

## License
MIT


