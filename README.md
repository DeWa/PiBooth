# PiBooth


## Installation

You need to install these dependencies
``
sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
   pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   python-setuptools libgstreamer1.0-dev git-core \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} python-dev libmtdev-dev \
   xclip xsel
``

Change Raspbi touchscreen to default touch method
``
vim ~/.kivy/config.ini
mouse = mouse
mtdev_%(name)s = probesysfs,provider=mtdev
hid_%(name)s = probesysfs,provider=hidinput
``

Install dependencies of Raspbi camera
``
sudo apt-get install python-gst0.10 gstreamer0.10-plugins-good gstreamer0.10-plugins-ugly
``