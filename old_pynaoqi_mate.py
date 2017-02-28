#!/usr/bin/env python
from importlib import import_module
from naoqi import ALBroker

# Class that helps on calling naoqi different modules and methods
# by joining them all in the same place
# Author: Sammy Pfeiffer <Sammy.Pfeiffer at student.uts.edu>


class Mate(object):
    def __init__(self, robot_ip, robot_port):
        self.broker = ALBroker("mate_broker", "0.0.0.0",
                               0, robot_ip, robot_port)

        # Create a list of all available ALProxys
        # TODO: automate this list generation
        self.available_proxies = [
            "ALAnimatedSpeech",
            "ALAudioDevice",
            "ALAudioPlayer",
            "ALAudioPlayer",
            "ALAudioRecorder",
            "ALAudioSourceLocalization",
            "ALAutomaticVolume",
            "ALAutonomousLife",
            "ALAutonomousMoves",
            "ALBacklightingDetection",
            "ALBarcodeReader",
            "ALBasicAwareness",
            "ALBattery",
            "ALBehaviorManager",
            "ALBodyDetection3D",
            "ALBodyTemperature",
            "ALBonjour",
            "ALChestButton",
            "ALChoregrapheRecorder",
            "ALCloseObjectDetection",
            "ALColorBlobDetection",
            "ALConnectionManager",
            "ALDarknessDetection",
            "ALDebug",
            "ALDiagnosis",
            "ALDialog",
            "ALEngagementZones",
            "ALExpressiveListening",
            "ALFaceCharacteristics",
            "ALFaceDetection",
            "ALFaceTracker",
            "ALFastPersonTracking",
            "ALFileManager",
            "ALFindPersonHead",
            "ALFrameManager",
            "ALFsr",
            "ALGazeAnalysis",
            "ALHeadPoseAnalysis",
            "ALInfrared",
            "ALLandMarkDetection",
            "ALLaser",
            "ALLauncher",
            "ALLeds",
            "ALLocalization",
            "ALLogger",
            "ALMecaLogger",
            "ALMemory",
            "ALMemoryWatcher",
            "ALModularity",
            "ALMotion",
            "ALMotionRecorder",
            "ALMovementDetection3D",
            "ALMovementDetection",
            "ALNavigation",
            "ALNotificationManager",
            "ALObjectDetection",
            "ALPanoramaCompass",
            "ALPeoplePerception",
            "ALPhotoCapture",
            "ALPreferenceManager",
            "ALPreferences",
            "ALPwtiUpdate",
            "ALPythonBridge",
            "ALRedBallDetection",
            "ALRedBallTracker",
            "ALResourceManager",
            "ALRobotModel",
            "ALRobotPose",
            "ALRobotPosture",
            "ALSegmentation3D",
            "ALSensors",
            "ALServiceManager",
            "ALSittingPeopleDetection",
            "ALSonar",
            "ALSoundDetection",
            "ALSoundLocalization",
            "ALSpeechRecognition",
            "ALStore",
            "ALSystem",
            "ALTactileGesture",
            "ALTelepathe",
            "ALTextToSpeech",
            "ALTextToSpeech",
            "ALTouch",
            "ALTracker",
            "ALUserSession",
            "ALVideoDevice",
            "ALVideoRecorder",
            "ALVisionRecognition",
            "ALVisionToolbox",
            "ALVisualCompass",
            "ALVisualSpaceHistory",
            "ALWavingDetection",
            "ALWorldRepresentation",
            "AudioFilterLoader",
            "DCM",
            "PackageManager"]

        self.import_and_lazy_instance_all()

    def import_all(self):
        # Import all Proxies...
        for proxy in self.available_proxies:
            # importing module
            mod = import_module(proxy)
            # getting class
            _class = getattr(mod, proxy)
            # Instantiating the proxy
            try:
                setattr(self, proxy, _class)
                print "Added class of: " + proxy
            except RuntimeError as e:
                if "Can't find service" in str(e):
                    print proxy + " has no ALProxy."
                else:
                    raise e
                continue

    def import_and_lazy_instance_all(self):
        # Instantiate all Proxies...
        for proxy in self.available_proxies:
            # importing module
            mod = import_module(proxy)
            # getting class
            _class = getattr(mod, proxy)
            # Instantiating the proxy
            try:
                class_instance = _class()
                # delete_non_user_friendly_methods(class_instance)
                setattr(self, proxy, class_instance)
                print "Added lazy instance of: " + proxy
            except RuntimeError as e:
                if "Can't find service" in str(e):
                    print proxy + " has no ALProxy."
                else:
                    raise e
                continue


if __name__ == '__main__':
    m = Mate("138.25.61.99", 9559)
