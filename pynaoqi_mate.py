#!/usr/bin/env python
from naoqi import ALBroker
from ALAnimatedSpeech import ALAnimatedSpeech
from ALAudioDevice import ALAudioDevice
from ALAudioPlayer import ALAudioPlayer
from ALAudioRecorder import ALAudioRecorder
from ALAudioSourceLocalization import ALAudioSourceLocalization
from ALAutomaticVolume import ALAutomaticVolume
from ALAutonomousLife import ALAutonomousLife
from ALAutonomousMoves import ALAutonomousMoves
from ALBacklightingDetection import ALBacklightingDetection
from ALBarcodeReader import ALBarcodeReader
from ALBasicAwareness import ALBasicAwareness
from ALBattery import ALBattery
from ALBehaviorManager import ALBehaviorManager
from ALBodyDetection3D import ALBodyDetection3D
from ALBodyTemperature import ALBodyTemperature
from ALBonjour import ALBonjour
from ALChestButton import ALChestButton
from ALChoregrapheRecorder import ALChoregrapheRecorder
from ALCloseObjectDetection import ALCloseObjectDetection
from ALColorBlobDetection import ALColorBlobDetection
from ALConnectionManager import ALConnectionManager
from ALDarknessDetection import ALDarknessDetection
from ALDebug import ALDebug
from ALDiagnosis import ALDiagnosis
from ALDialog import ALDialog
from ALEngagementZones import ALEngagementZones
from ALExpressiveListening import ALExpressiveListening
from ALFaceCharacteristics import ALFaceCharacteristics
from ALFaceDetection import ALFaceDetection
from ALFaceTracker import ALFaceTracker
from ALFastPersonTracking import ALFastPersonTracking
from ALFileManager import ALFileManager
from ALFindPersonHead import ALFindPersonHead
from ALFrameManager import ALFrameManager
from ALFsr import ALFsr
from ALGazeAnalysis import ALGazeAnalysis
from ALHeadPoseAnalysis import ALHeadPoseAnalysis
from ALInfrared import ALInfrared
from ALLandMarkDetection import ALLandMarkDetection
from ALLaser import ALLaser
from ALLauncher import ALLauncher
from ALLeds import ALLeds
from ALLocalization import ALLocalization
from ALLogger import ALLogger
from ALMecaLogger import ALMecaLogger
from ALMemory import ALMemory
from ALMemoryWatcher import ALMemoryWatcher
from ALModularity import ALModularity
from ALMotion import ALMotion
from ALMotionRecorder import ALMotionRecorder
from ALMovementDetection3D import ALMovementDetection3D
from ALMovementDetection import ALMovementDetection
from ALNavigation import ALNavigation
from ALNotificationManager import ALNotificationManager
from ALObjectDetection import ALObjectDetection
from ALPanoramaCompass import ALPanoramaCompass
from ALPeoplePerception import ALPeoplePerception
from ALPhotoCapture import ALPhotoCapture
from ALPreferenceManager import ALPreferenceManager
from ALPreferences import ALPreferences
from ALPwtiUpdate import ALPwtiUpdate
from ALPythonBridge import ALPythonBridge
from ALRedBallDetection import ALRedBallDetection
from ALRedBallTracker import ALRedBallTracker
from ALResourceManager import ALResourceManager
from ALRobotModel import ALRobotModel
from ALRobotPose import ALRobotPose
from ALRobotPosture import ALRobotPosture
from ALSegmentation3D import ALSegmentation3D
from ALSensors import ALSensors
from ALServiceManager import ALServiceManager
from ALSittingPeopleDetection import ALSittingPeopleDetection
from ALSonar import ALSonar
from ALSoundDetection import ALSoundDetection
from ALSoundLocalization import ALSoundLocalization
from ALSpeechRecognition import ALSpeechRecognition
from ALStore import ALStore
from ALSystem import ALSystem
from ALTactileGesture import ALTactileGesture
from ALTelepathe import ALTelepathe
from ALTextToSpeech import ALTextToSpeech
from ALTouch import ALTouch
from ALTracker import ALTracker
from ALUserSession import ALUserSession
from ALVideoDevice import ALVideoDevice
from ALVideoRecorder import ALVideoRecorder
from ALVisionRecognition import ALVisionRecognition
from ALVisionToolbox import ALVisionToolbox
from ALVisualCompass import ALVisualCompass
from ALVisualSpaceHistory import ALVisualSpaceHistory
from ALWavingDetection import ALWavingDetection
from ALWorldRepresentation import ALWorldRepresentation
from AudioFilterLoader import AudioFilterLoader
from DCM import DCM
from PackageManager import PackageManager


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
