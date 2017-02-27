# pynaoqi_mate
Developing with pynaoqi can be frustrating because of the lack of **autocompletion** and **docstrings** while coding either using _iPython_ or your _IDE (PyCharm, SublimeText, vim...)_.

No worries! Here comes your mate **pynaoqi_mate**.

It's a set of generated classes with all the methods from the C++ SDK header files with docstrings to use the ALProxy modules as if they were normal Python classes even though they still execute remotely.

**Note**: Further testing needed.

# Installation
Clone this repository somewhere and add the path of the folder `naoqi_proxy_python_classes` to your `PYTHONPATH`. For example:

```
cd ~
git clone https://github.com/uts-magic-lab/pynaoqi_mate
export PYTHONPATH=$PYTHONPATH:~/pynaoqi_mate/naoqi_proxy_python_classes
```

You may probably want to append it to your `.bashrc`.

And you may want to add it to your robot too if you want to run the scripts as they are from inside of the robot.

# Usage
Well, you have a big bunch of classes to choose from:

```
ALAnimatedSpeech.py           ALDialog.py               ALMotion.py                  ALSonar.py
ALAudioDevice.py              ALEngagementZones.py      ALMotionRecorder.py          ALSoundDetection.py
ALAudioPlayer.py              ALExpressiveListening.py  ALMovementDetection3D.py     ALSoundLocalization.py
ALAudioRecorder.py            ALFaceCharacteristics.py  ALMovementDetection.py       ALSpeechRecognition.py
ALAudioSourceLocalization.py  ALFaceDetection.py        ALNavigation.py              ALStore.py
ALAutomaticVolume.py          ALFaceTracker.py          ALNotificationManager.py     ALSystem.py
ALAutonomousLife.py           ALFastPersonTracking.py   ALObjectDetection.py         ALTactileGesture.py
ALAutonomousMoves.py          ALFileManager.py          ALPanoramaCompass.py         ALTelepathe.py
ALBacklightingDetection.py    ALFindPersonHead.py       ALPeoplePerception.py        ALTextToSpeech.py
ALBarcodeReader.py            ALFrameManager.py         ALPhotoCapture.py            ALTouch.py
ALBasicAwareness.py           ALFsr.py                  ALPreferenceManager.py       ALTracker.py
ALBattery.py                  ALGazeAnalysis.py         ALPreferences.py             ALUserSession.py
ALBehaviorManager.py          ALHeadPoseAnalysis.py     ALPwtiUpdate.py              ALVideoDevice.py
ALBodyDetection3D.py          ALInfrared.py             ALPythonBridge.py            ALVideoRecorder.py
ALBodyTemperature.py          ALLandMarkDetection.py    ALRedBallDetection.py        ALVisionRecognition.py
ALBonjour.py                  ALLaser.py                ALRedBallTracker.py          ALVisionToolbox.py
ALChestButton.py              ALLauncher.py             ALResourceManager.py         ALVisualCompass.py
ALChoregrapheRecorder.py      ALLeds.py                 ALRobotModel.py              ALVisualSpaceHistory.py
ALCloseObjectDetection.py     ALLocalization.py         ALRobotPose.py               ALWavingDetection.py
ALColorBlobDetection.py       ALLogger.py               ALRobotPosture.py            ALWorldRepresentation.py
ALConnectionManager.py        ALMecaLogger.py           ALSegmentation3D.py          AudioFilterLoader.py
ALDarknessDetection.py        ALMemory.py               ALSensors.py                 class_skeleton.py
ALDebug.py                    ALMemoryWatcher.py        ALServiceManager.py          DCM.py
ALDiagnosis.py                ALModularity.py           ALSittingPeopleDetection.py  PackageManager.py
```

You could do for example (iPython output):

```python
In [1]: from ALTextToSpeech import ALTextToSpeech 

In [2]: ALTextToSpeech.
ALTextToSpeech.disableNotifications     ALTextToSpeech.locale
ALTextToSpeech.enableNotifications      ALTextToSpeech.mro
ALTextToSpeech.exit                     ALTextToSpeech.pCall
ALTextToSpeech.getAvailableLanguages    ALTextToSpeech.ping
ALTextToSpeech.getAvailableVoices       ALTextToSpeech.py
ALTextToSpeech.getBrokerName            ALTextToSpeech.pyc
ALTextToSpeech.getGenericProxy          ALTextToSpeech.resetSpeed
ALTextToSpeech.getLanguage              ALTextToSpeech.say
ALTextToSpeech.getLanguageEncoding      ALTextToSpeech.sayToFile
ALTextToSpeech.getMethodHelp            ALTextToSpeech.sayToFileAndPlay
ALTextToSpeech.getMethodList            ALTextToSpeech.setLanguage
ALTextToSpeech.getModuleHelp            ALTextToSpeech.setLanguageDefaultVoice
ALTextToSpeech.getParameter             ALTextToSpeech.setParameter
ALTextToSpeech.getSupportedLanguages    ALTextToSpeech.setVoice
ALTextToSpeech.getUsage                 ALTextToSpeech.setVolume
ALTextToSpeech.getVoice                 ALTextToSpeech.stop
ALTextToSpeech.getVolume                ALTextToSpeech.stopAll
ALTextToSpeech.isRunning                ALTextToSpeech.version
ALTextToSpeech.loadVoicePreference      ALTextToSpeech.wait

In [2]: ALTextToSpeech.say?
Type:       instancemethod
String Form:<unbound method ALTextToSpeech.say>
File:       /home/sam/pynaoqi_mate/naoqi_proxy_python_classes/ALTextToSpeech.py
Definition: ALTextToSpeech.say(self, stringToSay, language)
Docstring:
Performs the text-to-speech operations in a specific language: it takes a std::string as input and outputs a sound in both speakers. String encoding must be UTF8. Once the text is said, the language is set back to its initial value.

:param str stringToSay: Text to say, encoded in UTF-8.
:param str language: Language used to say the text.

In [3]: from naoqi import ALBroker

In [4]: myBroker = ALBroker("myBroker", "0.0.0.0", 0, ROBOT_IP, NAOQI_PORT)

In [5]: tts = ALTextToSpeech()

In [6]: tts.say("This is cool!")

```

# Regeneration of the classes

Just download the C++ SDK, localize the folder `naoqi-sdk-2.1.4.13-linux64/include/alproxies` and run `generate_python_classes.py` from inside of that folder (just copy the file in there). It will parse `*proxy.h` header files using `CppHeaderParser`.

You'll need to install it if you don't have it:

    sudo pip install CppHeaderParser

When you execute it you should see a lot of output like:

```
Analysing header file: ./alledsproxy.h
Number of public methods 36
The remote class is called: ALLeds
And has the methods (ignoring constructors and destructors):
                           ...
------------------------------------------------------
  earLedsSetAngle
  C++        : void earLedsSetAngle ( const int & degrees , const float & duration , const bool & leaveOnAtEnd ) ;
  Params 3:      degrees (int) duration (float) leaveOnAtEnd (bool) 
  Return type: void
  Docs:        
       Summary: An animation to show a direction with the ears.
       Params:  [{'param_name': 'degrees', 'param_description': 'The angle you want to show in degrees (int). 0 is up, 90 is forwards, 180 is down and 270 is back.'}, {'param_name': 'duration', 'param_description': 'The duration in seconds of the animation.'}, {'param_name': 'leaveOnAtEnd', 'param_description': 'If true the last led is left on at the end of the animation.'}]
       Returns:

                           ...

------------------------------------------------------
  getIntensity
  C++        : AL::ALValue getIntensity ( const std::string & name ) ;
  Params 1:      name (std::string) 
  Return type: AL::ALValue
  Docs:        
       Summary: Gets the intensity of a LED or device
       Params:  [{'param_name': 'name', 'param_description': 'The name of the LED or Group.'}]
       Returns: The intensity of the LED or Group.
                           ...
```