#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alvisiontoolboxproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


# To not instance network connections until we actually want to
# do a proxy call
def lazy_init(fn):
    def init_if_needed(self, *args, **kwargs):
        if not self.proxy:
            self.proxy = ALProxy("ALVisionToolbox")
        return fn(self, *args, **kwargs)
    # Preserve method name and docs
    init_if_needed.__name__ = fn.__name__
    init_if_needed.__doc__ = fn.__doc__
    return init_if_needed


class ALVisionToolbox(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALVisionToolbox")

    @lazy_init
    def backlighting(self):
        """Indicates if we might be in backlighting conditions.

        :returns int: 0: no backlight - 1: possible backlight - 2 and more: backlight identified
        """
        return self.proxy.backlighting()

    @lazy_init
    def halfPress(self):
        """Prepare camera for shooting (like the auto-focus on standard and digital cameras)
        """
        return self.proxy.halfPress()

    @lazy_init
    def isItDark(self):
        """Tell if it is dark around.

        :returns int: [0;4] outdoor - [5;100] indoor bright - [101;127] indoor artificial light - [128;210] indoor weak lights - [211;255] dark place
        """
        return self.proxy.isItDark()

    @lazy_init
    def isVideoRecording(self):
        """Are we currently recording a video with startVideoRecord() or startVideoRecord_adv().

        :returns bool: True/False
        """
        return self.proxy.isVideoRecording()

    @lazy_init
    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    @lazy_init
    def setWhiteBalance(self, camera):
        """Set white balance by using Nao's white hands as reference.

        :param int camera: Camera we want to set white balance to : [0] top - [1] bottom - [2] both
        """
        return self.proxy.setWhiteBalance(camera)

    @lazy_init
    def startVideoRecord(self, videoName):
        """Start recording a video. The .avi video is stored on the robot in the \"/home/nao/.local/share/naoqi/vision\" folder. The record should be stopped by calling stopVideoRecord(). Resolution: 320*240, MJPG format, frame rate ~10-15 fps. Please note that only one record at a time can be made.

        :param str videoName: Name of the video file to be recorded.
        """
        return self.proxy.startVideoRecord(videoName)

    @lazy_init
    def startVideoRecord_adv(self, videoName, framerate, format, resIndex, numFrames):
        """Start recording a video, with advanced options. Please note that only one record at a time can be made.

        :param str videoName: Name of the video file to be recorded.
        :param float framerate: Record frame rate [0.1-50.0]. Warning: MJPG format requires framerate greater than 2.0.
        :param str format: ARV = raw YUV422 format; IYUV = raw avi, MJPG = compressed avi.
        :param int resIndex: Resolution index. 0 = 160*120, 1 = 320*240, 2 = 640*480
        :param int numFrames: Number of frames to record. If less than 0, it records until stopVideoRecord() is called.
        """
        return self.proxy.startVideoRecord_adv(videoName, framerate, format, resIndex, numFrames)

    @lazy_init
    def stopTPR(self, pathAndNameRoot, imageRecordFormat):
        """Stop an instance of takePictureRegularly()

        :param str pathAndNameRoot: path and name root of the file we want to stop recording
        :param str imageRecordFormat: formats of the file we want to stop recording
        """
        return self.proxy.stopTPR(pathAndNameRoot, imageRecordFormat)

    @lazy_init
    def stopVideoRecord(self):
        """Stop a video record that was launched with startVideoRecord() or startVideoRecord_adv(). The function returns the number of frames that were recorded, as well as the video absolute file name.

        :returns AL::ALValue: Array of two elements [numRecordedFrames, recordAbsolutePath]
        """
        return self.proxy.stopVideoRecord()

    @lazy_init
    def takePicture(self):
        """Shoot 3 successives pictures and place them in the \"/home/nao/recordings/cameras/\" folder. If halfPress has not been called before, it will take longer between click and shoot.
        """
        return self.proxy.takePicture()

    @lazy_init
    def takePictureRegularly(self, secondsBetweenTwoShots, pathAndNameRoot, overwriteImage, imageRecordFormat, resolution):
        """Shoot regularly a picture to follow Nao's evolution in his environment

        :param float secondsBetweenTwoShots: how many seconds between two pictures?
        :param str pathAndNameRoot: path and the root of the name for the picture
        :param bool overwriteImage: do we need to overwrite the picture, or do we add a timestamp to the name?
        :param str imageRecordFormat: such as jpeg, bmp, png, etc.
        :param int resolution: resolution for the image (e.g. kQQVGA, kQVGA)
        """
        return self.proxy.takePictureRegularly(secondsBetweenTwoShots, pathAndNameRoot, overwriteImage, imageRecordFormat, resolution)

    @lazy_init
    def takePictures(self, numberOfPictures):
        """Shoot a specific number of successives pictures and place them in the \"/home/nao/recordings/cameras/\" folder. If halfPress has not been called before, it will take longer between click and shoot.

        :param int numberOfPictures: how many pictures you want to take
        """
        return self.proxy.takePictures(numberOfPictures)

    @lazy_init
    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        return self.proxy.version()
