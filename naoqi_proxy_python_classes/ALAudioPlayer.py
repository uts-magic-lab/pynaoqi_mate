#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alaudioplayerproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


# To not instance network connections until we actually want to
# do a proxy call
def lazy_init(fn):
    def init_if_needed(self, *args, **kwargs):
        if not self.proxy:
            self.proxy = ALProxy("ALAudioPlayer")
        return fn(self, *args, **kwargs)
    # Preserve method name and docs
    init_if_needed.__name__ = fn.__name__
    init_if_needed.__doc__ = fn.__doc__
    return init_if_needed


class ALAudioPlayer(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALAudioPlayer")

    @lazy_init
    def getCurrentPosition(self, playId):
        """Returns the position in the file which is currently played

        :param int playId: Id of the process which is playing the file
        :returns float: Position in the file in seconds
        """
        return self.proxy.getCurrentPosition(playId)

    @lazy_init
    def getFileLength(self, playId):
        """Returns the length of the file played

        :param int playId: Id of the process which is playing the file
        :returns float: Length of the file in seconds
        """
        return self.proxy.getFileLength(playId)

    @lazy_init
    def getInstalledSoundSetsList(self):
        """

        :returns std::vector<std::string>: 
        """
        return self.proxy.getInstalledSoundSetsList()

    @lazy_init
    def getLoadedFilesIds(self):
        """returns an array containing the Ids of the currently loaded files

        :returns std::vector<std::string>: Array containing the Ids of the files which has been loaded
        """
        return self.proxy.getLoadedFilesIds()

    @lazy_init
    def getLoadedFilesNames(self):
        """returns an array containing the names of the currently loaded files

        :returns std::vector<std::string>: Array containing the names of the files which has been loaded
        """
        return self.proxy.getLoadedFilesNames()

    @lazy_init
    def getLoadedSoundSetsList(self):
        """

        :returns std::vector<std::string>: 
        """
        return self.proxy.getLoadedSoundSetsList()

    @lazy_init
    def getMasterVolume(self):
        """Returns the master volume of the player

        :returns float: Volume of the master - range 0.0 to 1.0.
        """
        return self.proxy.getMasterVolume()

    @lazy_init
    def getSoundSetFileNames(self, setName):
        """Return the list of files contained in a sound set

        :param str setName: name of the set
        :returns std::vector<std::string>: 
        """
        return self.proxy.getSoundSetFileNames(setName)

    @lazy_init
    def getVolume(self, playId):
        """Returns the volume of the player

        :param int playId: Id of the process which is playing the file
        :returns float: Volume of the player - range 0.0 to 1.0.
        """
        return self.proxy.getVolume(playId)

    @lazy_init
    def goTo(self, playId, position):
        """Goes to a given position in a file which is playing.

        :param int playId: Id of the process which is playing the file
        :param float position: Position in the file (in second)
        """
        return self.proxy.goTo(playId, position)

    @lazy_init
    def isSoundSetFileInstalled(self, setName, soundName):
        """

        :param str setName: name of the set
        :param str soundName: name of the sound
        :returns bool: 
        """
        return self.proxy.isSoundSetFileInstalled(setName, soundName)

    @lazy_init
    def isSoundSetInstalled(self, setName):
        """

        :param str setName: name of the set
        :returns bool: 
        """
        return self.proxy.isSoundSetInstalled(setName)

    @lazy_init
    def loadFile(self, fileName):
        """Loads a file for ulterior playback

        :param str fileName: Path of the sound file (either mp3 or wav)
        :returns int: Id of the file which has been loaded. This file can then be played with the play function
        """
        return self.proxy.loadFile(fileName)

    @lazy_init
    def loadSoundSet(self, setName):
        """Load a sound set

        :param str setName: name of the set
        """
        return self.proxy.loadSoundSet(setName)

    @lazy_init
    def pause(self, id):
        """Pause a play back

        :param int id: Id of the process that is playing the file you want to put in pause
        """
        return self.proxy.pause(id)

    @lazy_init
    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    @lazy_init
    def play(self, id):
        """Starts the playback of a file preloaded with the loadFile function.

        :param int id: Id returned by the loadFile function
        """
        return self.proxy.play(id)

    @lazy_init
    def play2(self, id, volume, pan):
        """Starts the playback of a file preloaded with the loadFile function, with specific volume and audio balance

        :param int id: Id returned by the loadFile function
        :param float volume: volume of the sound file (must be between 0.0 and 1.0)
        :param float pan: audio balance of the sound file (-1.0 : left / 1.0 : right)
        """
        return self.proxy.play(id, volume, pan)

    @lazy_init
    def playFile(self, fileName):
        """Plays a wav or mp3 file

        :param str fileName: Path of the sound file
        """
        return self.proxy.playFile(fileName)

    @lazy_init
    def playFile2(self, fileName, volume, pan):
        """Plays a wav or mp3 file, with specific volume and audio balance

        :param str fileName: Path of the sound file
        :param float volume: volume of the sound file (must be between 0.0 and 1.0)
        :param float pan: audio balance of the sound file (-1.0 : left / 1.0 : right / 0.0 : centered)
        """
        return self.proxy.playFile(fileName, volume, pan)

    @lazy_init
    def playFileFromPosition(self, fileName, position):
        """Plays a wav or mp3 file from a given position in the file.

        :param str fileName: Name of the sound file
        :param float position: Position in second where the playing has to begin
        """
        return self.proxy.playFileFromPosition(fileName, position)

    @lazy_init
    def playFileFromPosition2(self, fileName, position, volume, pan):
        """Plays a wav or mp3 file from a given position in the file, with specific volume and audio balance

        :param str fileName: Name of the sound file
        :param float position: Position in second where the playing has to begin
        :param float volume: volume of the sound file (must be between 0.0 and 1.0)
        :param float pan: audio balance of the sound file (-1.0 : left / 1.0 : right)
        """
        return self.proxy.playFileFromPosition(fileName, position, volume, pan)

    @lazy_init
    def playFileInLoop(self, fileName):
        """Plays a wav or mp3 file in loop

        :param str fileName: Path of the sound file
        """
        return self.proxy.playFileInLoop(fileName)

    @lazy_init
    def playFileInLoop2(self, fileName, volume, pan):
        """Plays a wav or mp3 file in loop, with specific volume and audio balance

        :param str fileName: Path of the sound file
        :param float volume: volume of the sound file (must be between 0.0 and 1.0)
        :param float pan: audio balance of the sound file (-1.0 : left / 1.0 : right)
        """
        return self.proxy.playFileInLoop(fileName, volume, pan)

    @lazy_init
    def playInLoop(self, id):
        """Starts the playback in loop of a file preloaded with the loadFile function

        :param int id: Id returned by the loadFile function
        """
        return self.proxy.playInLoop(id)

    @lazy_init
    def playInLoop2(self, id, volume, pan):
        """Plays a wav or mp3 file in loop, with specific volume and audio balance

        :param int id: Id returned by the loadFile function
        :param float volume: volume of the sound file (must be between 0.0 and 1.0)
        :param float pan: audio balance of the sound file (-1.0 : left / 1.0 : right)
        """
        return self.proxy.playInLoop(id, volume, pan)

    @lazy_init
    def playSine(self, frequence, gain, pan, duration):
        """Play a sine wave which specified caracteristics.

        :param int frequence: Frequence in Hertz
        :param int gain: Volume Gain between 0 and 100
        :param int pan: Stereo Pan set to either {-1,0,+1}
        :param float duration: Duration of the sine wave in seconds
        """
        return self.proxy.playSine(frequence, gain, pan, duration)

    @lazy_init
    def playSoundSetFile(self, fileName):
        """Plays a file contained in one of the sound sets loaded

        :param str fileName: Name of the file without extension
        """
        return self.proxy.playSoundSetFile(fileName)

    @lazy_init
    def playSoundSetFile2(self, soundSetName, fileName):
        """Plays a file contained in a given sound set

        :param str soundSetName: Name of the soundset
        :param str fileName: Name of the file without extension
        """
        return self.proxy.playSoundSetFile(soundSetName, fileName)

    @lazy_init
    def playSoundSetFile3(self, soundSetName, fileName, position, volume, pan, loop):
        """Plays a file contained in a given sound set

        :param str soundSetName: Name of the soundset
        :param str fileName: Name of the file without extension
        :param float position: Position in second where the playing has to begin
        :param float volume: volume of the sound file (must be between 0.0 and 1.0)
        :param float pan: audio balance of the sound file (-1.0 : left / 1.0 : right)
        :param bool loop: specify if the file must be played in loop
        """
        return self.proxy.playSoundSetFile(soundSetName, fileName, position, volume, pan, loop)

    @lazy_init
    def playSoundSetFile4(self, fileName, position, volume, pan, loop):
        """Plays a file contained in a given sound set

        :param str fileName: Name of the file without extension
        :param float position: Position in second where the playing has to begin
        :param float volume: volume of the sound file (must be between 0.0 and 1.0)
        :param float pan: audio balance of the sound file (-1.0 : left / 1.0 : right)
        :param bool loop: specify if the file must be played in loop
        """
        return self.proxy.playSoundSetFile(fileName, position, volume, pan, loop)

    @lazy_init
    def playWebStream(self, streamName, arg2, arg3):
        """Starts the playback of a wab audio stream

        :param str streamName: Path of the web audio stream
        :param float arg2: arg
        :param float arg3: arg
        """
        return self.proxy.playWebStream(streamName, arg2, arg3)

    @lazy_init
    def setMasterVolume(self, volume):
        """Sets the master volume of the player

        :param float volume: Volume - range 0.0 to 1.0
        """
        return self.proxy.setMasterVolume(volume)

    @lazy_init
    def setPanorama(self, arg1):
        """sets the audio panorama : -1 for left speaker / 1 for right speaker

        :param float arg1: arg
        """
        return self.proxy.setPanorama(arg1)

    @lazy_init
    def setVolume(self, id, volume):
        """Sets the volume of the player

        :param int id: Id of the process that is playing the file you want to put louder or less loud
        :param float volume: Volume - range 0.0 to 1.0
        """
        return self.proxy.setVolume(id, volume)

    @lazy_init
    def stopAll(self):
        """Stops all the files that are currently playing.
        """
        return self.proxy.stopAll()

    @lazy_init
    def unloadAllFiles(self):
        """unloads all the files already loaded.
        """
        return self.proxy.unloadAllFiles()

    @lazy_init
    def unloadFile(self, id):
        """unloads a file previously loaded with the loadFile function

        :param int id: Id returned by the loadFile function
        """
        return self.proxy.unloadFile(id)

    @lazy_init
    def unloadSoundSet(self, setName):
        """Unload a sound set

        :param str setName: name of the set
        """
        return self.proxy.unloadSoundSet(setName)

    @lazy_init
    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        return self.proxy.version()
