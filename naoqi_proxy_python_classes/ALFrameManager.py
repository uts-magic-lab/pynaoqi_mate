#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alframemanagerproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


# To not instance network connections until we actually want to
# do a proxy call
def lazy_init(fn):
    def init_if_needed(self, *args, **kwargs):
        if not self.proxy:
            self.proxy = ALProxy("ALFrameManager")
        return fn(self, *args, **kwargs)
    # Preserve method name and docs
    init_if_needed.__name__ = fn.__name__
    init_if_needed.__doc__ = fn.__doc__
    return init_if_needed


class ALFrameManager(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALFrameManager")

    @lazy_init
    def behaviors(self):
        """List all behaviors currently handled by the frame manager.

        :returns std::vector<std::string>: a set listing all behavior ids
        """
        return self.proxy.behaviors()

    @lazy_init
    def cleanBehaviors(self):
        """Stop playing any behavior in FrameManager, and delete all of them.
        """
        return self.proxy.cleanBehaviors()

    @lazy_init
    def completeBehavior(self, id):
        """It will play a behavior and block until the behavior is finished. Note that it can block forever if the behavior output is never called.

        :param str id: The id of the box.
        """
        return self.proxy.completeBehavior(id)

    @lazy_init
    def createTimeline(self, timelineContent):
        """Creates a timeline.

        :param str timelineContent: The timeline content (in XML format).
        :returns str: return a unique identifier for the created box that contains the timeline. You must call deleteBehavior on it at some point. DEPRECATED since 1.14
        """
        return self.proxy.createTimeline(timelineContent)

    @lazy_init
    def deleteBehavior(self, id):
        """Deletes a behavior (meaning a box). Stop the whole behavior contained in this box first.

        :param str id: The id of the box to delete.
        """
        return self.proxy.deleteBehavior(id)

    @lazy_init
    def exitBehavior(self, id):
        """Exit the reading of a timeline contained in a given box

        :param str id: The id of the box.
        """
        return self.proxy.exitBehavior(id)

    @lazy_init
    def getBehaviorPath(self, id):
        """Returns a playing behavior absolute path.

        :param str id: The id of the behavior.
        :returns str: Returns the absolute path of given behavior.
        """
        return self.proxy.getBehaviorPath(id)

    @lazy_init
    def getMotionLength(self, id):
        """Returns in seconds, the duration of a given movement stored in a box. Returns 0 if the behavior has no motion layers.  DEPRECATED since 1.14

        :param str id: The id of the box.
        :returns float: Returns the time in seconds.
        """
        return self.proxy.getMotionLength(id)

    @lazy_init
    def getTimelineFps(self, id):
        """Gets the FPS of a given timeline. DEPRECATED since 1.14

        :param str id: The id of the timeline.
        :returns int: Returns the timeline's FPS.
        """
        return self.proxy.getTimelineFps(id)

    @lazy_init
    def gotoAndPlay(self, id, frame):
        """Goes to a certain frame and continue playing. DEPRECATED since 1.14

        :param str id: The id of the box containing the box.
        :param str frame: The behavior frame name we want the timeline to go to. If will jump to the starting index of the name given.
        """
        return self.proxy.gotoAndPlay(id, frame)

    @lazy_init
    def gotoAndPlay2(self, id, frame):
        """Goes to a certain frame and continue playing. DEPRECATED since 1.14

        :param str id: The id of the box containing the box.
        :param int frame: The frame we want the timeline to go to.
        """
        return self.proxy.gotoAndPlay(id, frame)

    @lazy_init
    def gotoAndStop(self, id, frame):
        """Goes to a certain frame and pause. DEPRECATED since 1.14

        :param str id: The id of the box containing the box.
        :param str frame: The behavior frame name we want the timeline to go to. If will jump to the starting index of the name given.
        """
        return self.proxy.gotoAndStop(id, frame)

    @lazy_init
    def gotoAndStop2(self, id, frame):
        """Goes to a certain frame and pause. DEPRECATED since 1.14

        :param str id: The id of the box containing the box.
        :param int frame: The frame we want the timeline to go to.
        """
        return self.proxy.gotoAndStop(id, frame)

    @lazy_init
    def isBehaviorRunning(self, id):
        """Tells whether the behavior is running

        :param str id: The id of the behavior to check
        :returns bool: True if the behavior is running, false otherwise
        """
        return self.proxy.isBehaviorRunning(id)

    @lazy_init
    def newBehavior(self, path, xmlFile):
        """Creates a new behavior, from a box found in an xml file. Note that you have to give the xml file contents, so this method is not very user friendly. You have to open the file, and send the string that matches the file contents if you are working from a file. You probably want to use newBehaviorFromFile instead. DEPRECATED since 1.14

        :param str path: The path to reach the box to instantiate in the project ("" if root).
        :param str xmlFile: The choregraphe project (in plain text for the moment).
        :returns str: return a unique identifier for the created box.
        """
        return self.proxy.newBehavior(path, xmlFile)

    @lazy_init
    def newBehaviorFromChoregraphe(self):
        """Creates a new behavior, from the current Choregraphe behavior 0(uploaded to /tmp/currentChoregrapheBehavior/behavior.xar). DEPRECATED since 1.14

        :returns str: return a unique identifier for the created behavior
        """
        return self.proxy.newBehaviorFromChoregraphe()

    @lazy_init
    def newBehaviorFromFile(self, xmlFilePath, behName):
        """Creates a new behavior, from a box found in an xml file stored in the robot.

        :param str xmlFilePath: Path to Xml file, ex : "/home/youhou/mybehavior.xar".
        :param str behName: 
        :returns str: return a unique identifier for the created box, that can be used by playBehavior
        """
        return self.proxy.newBehaviorFromFile(xmlFilePath, behName)

    @lazy_init
    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    @lazy_init
    def playBehavior(self, id):
        """Starts a behavior

        :param str id: The id of the box.
        """
        return self.proxy.playBehavior(id)

    @lazy_init
    def playTimeline(self, id):
        """Starts playing a timeline contained in a given box. If the box is a flow diagram, it will look for the first onStart input of type Bang, and stimulate it ! DEPRECATED since 1.14

        :param str id: The id of the box.
        """
        return self.proxy.playTimeline(id)

    @lazy_init
    def setTimelineFps(self, id, fps):
        """Sets the FPS of a given timeline. DEPRECATED since 1.14

        :param str id: The id of the timeline.
        :param int fps: The FPS to set.
        """
        return self.proxy.setTimelineFps(id, fps)

    @lazy_init
    def stopTimeline(self, id):
        """Stops playing a timeline contained in a given box, at the current frame. DEPRECATED since 1.14

        :param str id: The id of the box.
        """
        return self.proxy.stopTimeline(id)

    @lazy_init
    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        return self.proxy.version()
