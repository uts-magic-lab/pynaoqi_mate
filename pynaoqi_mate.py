#!/usr/bin/env python
from naoqi import ALBroker
from naoqi_proxy_python_classes.ALAnimatedSpeech import ALAnimatedSpeech
from naoqi_proxy_python_classes.ALAudioDevice import ALAudioDevice
from naoqi_proxy_python_classes.ALAudioPlayer import ALAudioPlayer
from naoqi_proxy_python_classes.ALAudioRecorder import ALAudioRecorder
from naoqi_proxy_python_classes.ALAudioSourceLocalization import ALAudioSourceLocalization
from naoqi_proxy_python_classes.ALAutomaticVolume import ALAutomaticVolume
from naoqi_proxy_python_classes.ALAutonomousLife import ALAutonomousLife
from naoqi_proxy_python_classes.ALAutonomousMoves import ALAutonomousMoves
from naoqi_proxy_python_classes.ALBacklightingDetection import ALBacklightingDetection
from naoqi_proxy_python_classes.ALBarcodeReader import ALBarcodeReader
from naoqi_proxy_python_classes.ALBasicAwareness import ALBasicAwareness
from naoqi_proxy_python_classes.ALBattery import ALBattery
from naoqi_proxy_python_classes.ALBehaviorManager import ALBehaviorManager
from naoqi_proxy_python_classes.ALBodyDetection3D import ALBodyDetection3D
from naoqi_proxy_python_classes.ALBodyTemperature import ALBodyTemperature
from naoqi_proxy_python_classes.ALBonjour import ALBonjour
from naoqi_proxy_python_classes.ALChestButton import ALChestButton
from naoqi_proxy_python_classes.ALChoregrapheRecorder import ALChoregrapheRecorder
from naoqi_proxy_python_classes.ALCloseObjectDetection import ALCloseObjectDetection
from naoqi_proxy_python_classes.ALColorBlobDetection import ALColorBlobDetection
from naoqi_proxy_python_classes.ALConnectionManager import ALConnectionManager
from naoqi_proxy_python_classes.ALDarknessDetection import ALDarknessDetection
from naoqi_proxy_python_classes.ALDebug import ALDebug
from naoqi_proxy_python_classes.ALDiagnosis import ALDiagnosis
from naoqi_proxy_python_classes.ALDialog import ALDialog
from naoqi_proxy_python_classes.ALEngagementZones import ALEngagementZones
from naoqi_proxy_python_classes.ALExpressiveListening import ALExpressiveListening
from naoqi_proxy_python_classes.ALFaceCharacteristics import ALFaceCharacteristics
from naoqi_proxy_python_classes.ALFaceDetection import ALFaceDetection
from naoqi_proxy_python_classes.ALFaceTracker import ALFaceTracker
from naoqi_proxy_python_classes.ALFastPersonTracking import ALFastPersonTracking
from naoqi_proxy_python_classes.ALFileManager import ALFileManager
from naoqi_proxy_python_classes.ALFindPersonHead import ALFindPersonHead
from naoqi_proxy_python_classes.ALFrameManager import ALFrameManager
from naoqi_proxy_python_classes.ALFsr import ALFsr
from naoqi_proxy_python_classes.ALGazeAnalysis import ALGazeAnalysis
from naoqi_proxy_python_classes.ALHeadPoseAnalysis import ALHeadPoseAnalysis
from naoqi_proxy_python_classes.ALInfrared import ALInfrared
from naoqi_proxy_python_classes.ALLandMarkDetection import ALLandMarkDetection
from naoqi_proxy_python_classes.ALLaser import ALLaser
from naoqi_proxy_python_classes.ALLauncher import ALLauncher
from naoqi_proxy_python_classes.ALLeds import ALLeds
from naoqi_proxy_python_classes.ALLocalization import ALLocalization
from naoqi_proxy_python_classes.ALLogger import ALLogger
from naoqi_proxy_python_classes.ALMecaLogger import ALMecaLogger
from naoqi_proxy_python_classes.ALMemory import ALMemory
from naoqi_proxy_python_classes.ALMemoryWatcher import ALMemoryWatcher
from naoqi_proxy_python_classes.ALModularity import ALModularity
from naoqi_proxy_python_classes.ALMotion import ALMotion
from naoqi_proxy_python_classes.ALMotionRecorder import ALMotionRecorder
from naoqi_proxy_python_classes.ALMovementDetection3D import ALMovementDetection3D
from naoqi_proxy_python_classes.ALMovementDetection import ALMovementDetection
from naoqi_proxy_python_classes.ALNavigation import ALNavigation
from naoqi_proxy_python_classes.ALNotificationManager import ALNotificationManager
from naoqi_proxy_python_classes.ALObjectDetection import ALObjectDetection
from naoqi_proxy_python_classes.ALPanoramaCompass import ALPanoramaCompass
from naoqi_proxy_python_classes.ALPeoplePerception import ALPeoplePerception
from naoqi_proxy_python_classes.ALPhotoCapture import ALPhotoCapture
from naoqi_proxy_python_classes.ALPreferenceManager import ALPreferenceManager
from naoqi_proxy_python_classes.ALPreferences import ALPreferences
from naoqi_proxy_python_classes.ALPwtiUpdate import ALPwtiUpdate
from naoqi_proxy_python_classes.ALPythonBridge import ALPythonBridge
from naoqi_proxy_python_classes.ALRecharge import ALRecharge
from naoqi_proxy_python_classes.ALRedBallDetection import ALRedBallDetection
from naoqi_proxy_python_classes.ALRedBallTracker import ALRedBallTracker
from naoqi_proxy_python_classes.ALResourceManager import ALResourceManager
from naoqi_proxy_python_classes.ALRobotModel import ALRobotModel
from naoqi_proxy_python_classes.ALRobotPose import ALRobotPose
from naoqi_proxy_python_classes.ALRobotPosture import ALRobotPosture
from naoqi_proxy_python_classes.ALSegmentation3D import ALSegmentation3D
from naoqi_proxy_python_classes.ALSensors import ALSensors
from naoqi_proxy_python_classes.ALServiceManager import ALServiceManager
from naoqi_proxy_python_classes.ALSittingPeopleDetection import ALSittingPeopleDetection
from naoqi_proxy_python_classes.ALSonar import ALSonar
from naoqi_proxy_python_classes.ALSoundDetection import ALSoundDetection
from naoqi_proxy_python_classes.ALSoundLocalization import ALSoundLocalization
from naoqi_proxy_python_classes.ALSpeechRecognition import ALSpeechRecognition
from naoqi_proxy_python_classes.ALStore import ALStore
from naoqi_proxy_python_classes.ALSystem import ALSystem
from naoqi_proxy_python_classes.ALTactileGesture import ALTactileGesture
from naoqi_proxy_python_classes.ALTelepathe import ALTelepathe
from naoqi_proxy_python_classes.ALTextToSpeech import ALTextToSpeech
from naoqi_proxy_python_classes.ALTouch import ALTouch
from naoqi_proxy_python_classes.ALTracker import ALTracker
from naoqi_proxy_python_classes.ALUserSession import ALUserSession
from naoqi_proxy_python_classes.ALVideoDevice import ALVideoDevice
from naoqi_proxy_python_classes.ALVideoRecorder import ALVideoRecorder
from naoqi_proxy_python_classes.ALVisionRecognition import ALVisionRecognition
from naoqi_proxy_python_classes.ALVisionToolbox import ALVisionToolbox
from naoqi_proxy_python_classes.ALVisualCompass import ALVisualCompass
from naoqi_proxy_python_classes.ALVisualSpaceHistory import ALVisualSpaceHistory
from naoqi_proxy_python_classes.ALWavingDetection import ALWavingDetection
from naoqi_proxy_python_classes.ALWorldRepresentation import ALWorldRepresentation
from naoqi_proxy_python_classes.AudioFilterLoader import AudioFilterLoader
from naoqi_proxy_python_classes.DCM import DCM
from naoqi_proxy_python_classes.PackageManager import PackageManager


# Class that helps on calling naoqi different modules and methods
# by joining them all in the same place
# This has been half generated, half cleaned up by hand
# Author: Sammy Pfeiffer <Sammy.Pfeiffer at student.uts.edu>


class Mate(object):
    """
    Your PyNAOQI mate class.
    """
    ALAnimatedSpeech = ALAnimatedSpeech()
    ALAudioDevice = ALAudioDevice()
    ALAudioPlayer = ALAudioPlayer()
    ALAudioRecorder = ALAudioRecorder()
    ALAudioSourceLocalization = ALAudioSourceLocalization()
    ALAutomaticVolume = ALAutomaticVolume()
    ALAutonomousLife = ALAutonomousLife()
    ALAutonomousMoves = ALAutonomousMoves()
    ALBacklightingDetection = ALBacklightingDetection()
    ALBarcodeReader = ALBarcodeReader()
    ALBasicAwareness = ALBasicAwareness()
    ALBattery = ALBattery()
    ALBehaviorManager = ALBehaviorManager()
    ALBodyDetection3D = ALBodyDetection3D()
    ALBodyTemperature = ALBodyTemperature()
    ALBonjour = ALBonjour()
    ALChestButton = ALChestButton()
    ALChoregrapheRecorder = ALChoregrapheRecorder()
    ALCloseObjectDetection = ALCloseObjectDetection()
    ALColorBlobDetection = ALColorBlobDetection()
    ALConnectionManager = ALConnectionManager()
    ALDarknessDetection = ALDarknessDetection()
    ALDebug = ALDebug()
    ALDiagnosis = ALDiagnosis()
    ALDialog = ALDialog()
    ALEngagementZones = ALEngagementZones()
    ALExpressiveListening = ALExpressiveListening()
    ALFaceCharacteristics = ALFaceCharacteristics()
    ALFaceDetection = ALFaceDetection()
    ALFaceTracker = ALFaceTracker()
    ALFastPersonTracking = ALFastPersonTracking()
    ALFileManager = ALFileManager()
    ALFindPersonHead = ALFindPersonHead()
    ALFrameManager = ALFrameManager()
    ALFsr = ALFsr()
    ALGazeAnalysis = ALGazeAnalysis()
    ALHeadPoseAnalysis = ALHeadPoseAnalysis()
    ALInfrared = ALInfrared()
    ALLandMarkDetection = ALLandMarkDetection()
    ALLaser = ALLaser()
    ALLauncher = ALLauncher()
    ALLeds = ALLeds()
    ALLocalization = ALLocalization()
    ALLogger = ALLogger()
    ALMecaLogger = ALMecaLogger()
    ALMemory = ALMemory()
    ALMemoryWatcher = ALMemoryWatcher()
    ALModularity = ALModularity()
    ALMotion = ALMotion()
    ALMotionRecorder = ALMotionRecorder()
    ALMovementDetection3D = ALMovementDetection3D()
    ALMovementDetection = ALMovementDetection()
    ALNavigation = ALNavigation()
    ALNotificationManager = ALNotificationManager()
    ALObjectDetection = ALObjectDetection()
    ALPanoramaCompass = ALPanoramaCompass()
    ALPeoplePerception = ALPeoplePerception()
    ALPhotoCapture = ALPhotoCapture()
    ALPreferenceManager = ALPreferenceManager()
    ALPreferences = ALPreferences()
    ALPwtiUpdate = ALPwtiUpdate()
    ALPythonBridge = ALPythonBridge()
    ALRecharge = ALRecharge()
    ALRedBallDetection = ALRedBallDetection()
    ALRedBallTracker = ALRedBallTracker()
    ALResourceManager = ALResourceManager()
    ALRobotModel = ALRobotModel()
    ALRobotPose = ALRobotPose()
    ALRobotPosture = ALRobotPosture()
    ALSegmentation3D = ALSegmentation3D()
    ALSensors = ALSensors()
    ALServiceManager = ALServiceManager()
    ALSittingPeopleDetection = ALSittingPeopleDetection()
    ALSonar = ALSonar()
    ALSoundDetection = ALSoundDetection()
    ALSoundLocalization = ALSoundLocalization()
    ALSpeechRecognition = ALSpeechRecognition()
    ALStore = ALStore()
    ALSystem = ALSystem()
    ALTactileGesture = ALTactileGesture()
    ALTelepathe = ALTelepathe()
    ALTextToSpeech = ALTextToSpeech()
    ALTouch = ALTouch()
    ALTracker = ALTracker()
    ALUserSession = ALUserSession()
    ALVideoDevice = ALVideoDevice()
    ALVideoRecorder = ALVideoRecorder()
    ALVisionRecognition = ALVisionRecognition()
    ALVisionToolbox = ALVisionToolbox()
    ALVisualCompass = ALVisualCompass()
    ALVisualSpaceHistory = ALVisualSpaceHistory()
    ALWavingDetection = ALWavingDetection()
    ALWorldRepresentation = ALWorldRepresentation()
    AudioFilterLoader = AudioFilterLoader()
    DCM = DCM()
    PackageManager = PackageManager()

    def __init__(self, robot_ip, robot_port):
        self.broker = ALBroker("mate_broker", "0.0.0.0",
                               0, robot_ip, robot_port)


if __name__ == '__main__':
    m = Mate("138.25.61.99", 9559)
