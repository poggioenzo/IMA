# MakeMeLaugh

*UniGe Project*


Deep learning project to detect what is funny in a video. Use of OpenCV
for face detection. The goal is to detect the humor of the user to give
him more similar content.

This application will be the first step for a laught application.
This part use a camera and OpenFace to get user's Action Unit

For more information please read the [report](https://github.com/poggioenzo/IMA/blob/master/report.pdf).

---

# The code
## How to run
1. Launch the IMA/scripts/main.py file : python3 main.py
2. Set an ID in console mode
3. (optionnal) If VLC is not localized, set the right directory with the view

Script description
==================

### apt install
VLC and ImageTk are needed by the application to play and record videos.
To install it :
```bash
sudo apt-get install vlc
sudo apt-get install python3-pil.imagetk
```

### Dependencies
This project use some standard library :
- [numpy](http://www.numpy.org/)
- [SQLAlchemy](http://docs.sqlalchemy.org/en/latest/)
- [pillow](https://pypi.python.org/pypi/Pillow/3.3.1)

To install it :
```bash
sudo pip3 install numpy
sudo pip3 install sqlalchemy
sudo pip3 install pillow
```

### Install OpenCV
go to http://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/
