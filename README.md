# pynaoqi_mate
Developing with pynaoqi can be frustrating because of the lack of **autocompletion** and **docstrings** while coding either using _iPython_ or your _IDE (PyCharm, SublimeText, vim...)_.

No worries! Here comes your mate **pynaoqi_mate**.

It's a set of generated classes with all the methods from the C++ SDK header files with docstrings to use the ALProxy modules as if they were normal Python classes even though they still execute remotely.

And also a handy class called **Mate** to easily explore all the modules and methods.


# Installation
Prerequisites:
* [pynaoqi](http://doc.aldebaran.com/2-1/dev/python/install_guide.html) installed.

Clone this repository somewhere and add the path of the main folder `pynaoqi_mate` to your `PYTHONPATH`. For example:

```bash
cd ~
git clone https://github.com/uts-magic-lab/pynaoqi_mate
export PYTHONPATH=$PYTHONPATH:~/pynaoqi_mate
```

You may probably want to append it to your `.bashrc`.

And you may want to add it to your robot too if you want to run the scripts as they are from inside of the robot.

# Usage
Check out the video as an example of usage where I follow this README instructions:

[![Video of the pynaoqi_mate](http://img.youtube.com/vi/ExDExxN7Qb4/0.jpg)](https://youtu.be/ExDExxN7Qb4)

Explore with iPython:

```python
In [1]: from pynaoqi_mate import Mate

In [2]: m = Mate("138.25.61.99", 9559)  # You need to connect to a robot
inaoqi-broker: construct at 0.0.0.0:0, parent : 138.25.61.99:9559
[I] 22566 qimessaging.session: Session listener created on tcp://0.0.0.0:0
[I] 22566 qimessaging.transportserver: TransportServer will listen on: tcp://172.17.0.1:39688
[I] 22566 qimessaging.transportserver: TransportServer will listen on: tcp://127.0.0.1:39688
[I] 22566 qimessaging.transportserver: TransportServer will listen on: tcp://138.25.61.100:39688

In [3]: m.  # Pressing tab you get all the modules
m.ALAnimatedSpeech           m.ALFindPersonHead           m.ALResourceManager
m.ALAudioDevice              m.ALFrameManager             m.ALRobotModel
m.ALAudioPlayer              m.ALFsr                      m.ALRobotPose
m.ALAudioRecorder            m.ALGazeAnalysis             m.ALRobotPosture
m.ALAudioSourceLocalization  m.ALHeadPoseAnalysis         m.ALSegmentation3D
m.ALAutomaticVolume          m.ALInfrared                 m.ALSensors
m.ALAutonomousLife           m.ALLandMarkDetection        m.ALServiceManager
m.ALAutonomousMoves          m.ALLaser                    m.ALSittingPeopleDetection
m.ALBacklightingDetection    m.ALLauncher                 m.ALSonar
m.ALBarcodeReader            m.ALLeds                     m.ALSoundDetection
m.ALBasicAwareness           m.ALLocalization             m.ALSoundLocalization
m.ALBattery                  m.ALLogger                   m.ALSpeechRecognition
m.ALBehaviorManager          m.ALMecaLogger               m.ALStore
m.ALBodyDetection3D          m.ALMemory                   m.ALSystem
m.ALBodyTemperature          m.ALMemoryWatcher            m.ALTactileGesture
m.ALBonjour                  m.ALModularity               m.ALTelepathe
m.ALChestButton              m.ALMotion                   m.ALTextToSpeech
m.ALChoregrapheRecorder      m.ALMotionRecorder           m.ALTouch
m.ALCloseObjectDetection     m.ALMovementDetection        m.ALTracker
m.ALColorBlobDetection       m.ALMovementDetection3D      m.ALUserSession
m.ALConnectionManager        m.ALNavigation               m.ALVideoDevice
m.ALDarknessDetection        m.ALNotificationManager      m.ALVideoRecorder
m.ALDebug                    m.ALObjectDetection          m.ALVisionRecognition
m.ALDiagnosis                m.ALPanoramaCompass          m.ALVisionToolbox
m.ALDialog                   m.ALPeoplePerception         m.ALVisualCompass
m.ALEngagementZones          m.ALPhotoCapture             m.ALVisualSpaceHistory
m.ALExpressiveListening      m.ALPreferenceManager        m.ALWavingDetection
m.ALFaceCharacteristics      m.ALPreferences              m.ALWorldRepresentation
m.ALFaceDetection            m.ALPwtiUpdate               m.AudioFilterLoader
m.ALFaceTracker              m.ALPythonBridge             m.DCM
m.ALFastPersonTracking       m.ALRedBallDetection         m.PackageManager
m.ALFileManager              m.ALRedBallTracker           m.broker

In [3]: m.ALTextToSpeech.  # Pressing tab you get all the methods
m.ALTextToSpeech.disableNotifications     m.ALTextToSpeech.proxy
m.ALTextToSpeech.enableNotifications      m.ALTextToSpeech.resetSpeed
m.ALTextToSpeech.getAvailableLanguages    m.ALTextToSpeech.say
m.ALTextToSpeech.getAvailableVoices       m.ALTextToSpeech.say2
m.ALTextToSpeech.getLanguage              m.ALTextToSpeech.sayToFile
m.ALTextToSpeech.getLanguageEncoding      m.ALTextToSpeech.sayToFileAndPlay
m.ALTextToSpeech.getParameter             m.ALTextToSpeech.setLanguage
m.ALTextToSpeech.getSupportedLanguages    m.ALTextToSpeech.setLanguageDefaultVoice
m.ALTextToSpeech.getVoice                 m.ALTextToSpeech.setParameter
m.ALTextToSpeech.getVolume                m.ALTextToSpeech.setVoice
m.ALTextToSpeech.loadVoicePreference      m.ALTextToSpeech.setVolume
m.ALTextToSpeech.locale                   m.ALTextToSpeech.stopAll
m.ALTextToSpeech.ping                     m.ALTextToSpeech.version

In [3]: m.ALTextToSpeech.getLa
m.ALTextToSpeech.getLanguage          m.ALTextToSpeech.getLanguageEncoding  

In [3]: m.ALTextToSpeech.getLanguage?  # With ? you get the docs
Type:       instancemethod
String Form:<bound method ALTextToSpeech.getLanguage of <naoqi_proxy_python_classes.ALTextToSpeech.ALTextToSpeech object at 0x7f76c6051310>>
File:       /home/sam/magiclab/nao_ws/pynaoqi_mate/naoqi_proxy_python_classes/ALTextToSpeech.py
Definition: m.ALTextToSpeech.getLanguage(self, *args, **kwargs)
Docstring:
Returns the language currently used by the text-to-speech engine.

:returns str: Language of the current voice.

In [4]: m.ALTextToSpeech.getLanguage()
Out[4]: 'English'

In [5]: m.ALTextToSpeech.say
m.ALTextToSpeech.say               m.ALTextToSpeech.sayToFile         
m.ALTextToSpeech.say2              m.ALTextToSpeech.sayToFileAndPlay  

In [5]: m.ALTextToSpeech.say?
Type:       instancemethod
String Form:<bound method ALTextToSpeech.say of <naoqi_proxy_python_classes.ALTextToSpeech.ALTextToSpeech object at 0x7f76c6051310>>
File:       /home/sam/magiclab/nao_ws/pynaoqi_mate/naoqi_proxy_python_classes/ALTextToSpeech.py
Definition: m.ALTextToSpeech.say(self, *args, **kwargs)
Docstring:
Performs the text-to-speech operations : it takes a std::string as input and outputs a sound in both speakers. String encoding must be UTF8.

:param str stringToSay: Text to say, encoded in UTF-8.

In [6]: m.ALTextToSpeech.say2?
Type:       instancemethod
String Form:<bound method ALTextToSpeech.say2 of <naoqi_proxy_python_classes.ALTextToSpeech.ALTextToSpeech object at 0x7f76c6051310>>
File:       /home/sam/magiclab/nao_ws/pynaoqi_mate/naoqi_proxy_python_classes/ALTextToSpeech.py
Definition: m.ALTextToSpeech.say2(self, *args, **kwargs)
Docstring:
Performs the text-to-speech operations in a specific language: it takes a std::string as input and outputs a sound in both speakers. String encoding must be UTF8. Once the text is said, the language is set back to its initial value.

:param str stringToSay: Text to say, encoded in UTF-8.
:param str language: Language used to say the text.

In [7]: m.ALTextToSpeech.say('This is terrific!')


```

Note that the first time you call a method of a module it will create the real `ALProxy` connection, so the first call _may_ be a bit slower. You can "warm up" the connection calling `force_connect()`.

# Regeneration of the classes

Just download the C++ SDK, localize the folder `naoqi-sdk-2.5.5.5-linux64/include/alproxies` and run `generate_python_classes.py` from inside of that folder (just copy the file in there) or giving it as the first parameter the folder path. It will parse `*proxy.h` header files using `CppHeaderParser`.

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

Note that [some methods are "blacklisted"](https://github.com/uts-magic-lab/pynaoqi_mate/blob/master/generate_python_classes.py#L195-L208) in the generator as they have no use in Python or are relatively dangerous to be used by accident.