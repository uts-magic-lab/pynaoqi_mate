#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/almodularityproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


# To not instance network connections until we actually want to
# do a proxy call
def lazy_init(fn):
    def init_if_needed(self, *args, **kwargs):
        if not self.proxy:
            self.proxy = ALProxy("ALModularity")
        return fn(self, *args, **kwargs)
    # Preserve method name and docs
    init_if_needed.__name__ = fn.__name__
    init_if_needed.__doc__ = fn.__doc__
    return init_if_needed


class ALModularity(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALModularity")

    @lazy_init
    def deleteFilter(self, name):
        """

        :param str name: The name of the filter.
        :returns bool: 
        """
        return self.proxy.deleteFilter(name)

    @lazy_init
    def deleteProcess(self, name):
        """

        :param str name: The name of the process.
        :returns bool: 
        """
        return self.proxy.deleteProcess(name)

    @lazy_init
    def deleteSource(self, name):
        """

        :param str name: The name of the source.
        :returns bool: 
        """
        return self.proxy.deleteSource(name)

    @lazy_init
    def disableProcess(self, name):
        """

        :param str name: The name of the process.
        :returns bool: 
        """
        return self.proxy.disableProcess(name)

    @lazy_init
    def enableProcess(self, name):
        """

        :param str name: The name of the process.
        :returns bool: 
        """
        return self.proxy.enableProcess(name)

    @lazy_init
    def getData(self, sink):
        """

        :param str sink: The name of the sink from where data must be extracted.
        :returns AL::ALValue: 
        """
        return self.proxy.getData(sink)

    @lazy_init
    def getDotGraph(self, filter, level):
        """

        :param str filter: The name of the filter to dump.
        :param int level: Maximum depth (-1 for unlimited depth)
        :returns AL::ALValue: 
        """
        return self.proxy.getDotGraph(filter, level)

    @lazy_init
    def getFilterDescription(self, name):
        """

        :param str name: The name of the filter.
        :returns str: 
        """
        return self.proxy.getFilterDescription(name)

    @lazy_init
    def getFilterInputs(self, name):
        """

        :param str name: The name of the filter.
        :returns AL::ALValue: 
        """
        return self.proxy.getFilterInputs(name)

    @lazy_init
    def getFilterOutputs(self, name):
        """

        :param str name: The name of the filter.
        :returns AL::ALValue: 
        """
        return self.proxy.getFilterOutputs(name)

    @lazy_init
    def getFilters(self):
        """

        :returns AL::ALValue: 
        """
        return self.proxy.getFilters()

    @lazy_init
    def getImageLocal(self, sink):
        """

        :param str sink: The name of the sink from where data must be extracted.
        """
        return self.proxy.getImageLocal(sink)

    @lazy_init
    def getImageRemote(self, sink):
        """

        :param str sink: The name of the sink from where data must be extracted.
        :returns AL::ALValue: 
        """
        return self.proxy.getImageRemote(sink)

    @lazy_init
    def getInstrumentationResult(self):
        """

        :returns str: 
        """
        return self.proxy.getInstrumentationResult()

    @lazy_init
    def getLastData(self, sink):
        """

        :param str sink: The name of the sink from where data must be extracted.
        :returns AL::ALValue: 
        """
        return self.proxy.getLastData(sink)

    @lazy_init
    def getModularity(self):
        """
        """
        return self.proxy.getModularity()

    @lazy_init
    def getProcessAggregatedSinks(self, name):
        """

        :param str name: The name of the process.
        :returns std::vector<std::string>: 
        """
        return self.proxy.getProcessAggregatedSinks(name)

    @lazy_init
    def getProcessDescription(self, name):
        """

        :param str name: The name of the process.
        :returns str: 
        """
        return self.proxy.getProcessDescription(name)

    @lazy_init
    def getProcessFrequency(self, name):
        """

        :param str name: The name of the process.
        :returns float: 
        """
        return self.proxy.getProcessFrequency(name)

    @lazy_init
    def getProcessPriority(self, name):
        """

        :param str name: The name of the process.
        :returns int: 
        """
        return self.proxy.getProcessPriority(name)

    @lazy_init
    def getProcessSinks(self, name):
        """

        :param str name: The name of the process.
        :returns std::vector<std::string>: 
        """
        return self.proxy.getProcessSinks(name)

    @lazy_init
    def getProcessSources(self, name):
        """

        :param str name: The name of the process.
        :returns std::vector<std::string>: 
        """
        return self.proxy.getProcessSources(name)

    @lazy_init
    def getProcesses(self):
        """

        :returns std::vector<std::string>: 
        """
        return self.proxy.getProcesses()

    @lazy_init
    def getRobotHeightOffset(self):
        """

        :returns float: 
        """
        return self.proxy.getRobotHeightOffset()

    @lazy_init
    def getScheduledJobs(self):
        """

        :returns std::vector<std::string>: 
        """
        return self.proxy.getScheduledJobs()

    @lazy_init
    def getSourceFrequency(self, name):
        """

        :param str name: The name of the source.
        :returns float: 
        """
        return self.proxy.getSourceFrequency(name)

    @lazy_init
    def getSources(self):
        """

        :returns std::vector<std::string>: 
        """
        return self.proxy.getSources()

    @lazy_init
    def isProcessEnable(self, name):
        """

        :param str name: The name of the process.
        :returns bool: 
        """
        return self.proxy.isProcessEnable(name)

    @lazy_init
    def isProcessZombie(self, name):
        """

        :param str name: The name of the process.
        :returns bool: 
        """
        return self.proxy.isProcessZombie(name)

    @lazy_init
    def isProcesses(self, name):
        """

        :param str name: The name of the process.
        :returns bool: 
        """
        return self.proxy.isProcesses(name)

    @lazy_init
    def isSourceBinded(self, name):
        """

        :param str name: The name of the source.
        :returns bool: 
        """
        return self.proxy.isSourceBinded(name)

    @lazy_init
    def loadProgram(self, program):
        """

        :param str program: The code that will be used by Modularity to generate a part of the graph.
        :returns bool: 
        """
        return self.proxy.loadProgram(program)

    @lazy_init
    def loadProgramFromFile(self, arg1):
        """

        :param str arg1: arg
        :returns bool: 
        """
        return self.proxy.loadProgramFromFile(arg1)

    @lazy_init
    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    @lazy_init
    def resetProcess(self, name):
        """

        :param str name: The name of the process to reset.
        :returns bool: 
        """
        return self.proxy.resetProcess(name)

    @lazy_init
    def setProcessFrequency(self, name, priority):
        """

        :param str name: The name of the process.
        :param float priority: The new frequency of the process.
        :returns bool: 
        """
        return self.proxy.setProcessFrequency(name, priority)

    @lazy_init
    def setProcessPriority(self, name, priority):
        """

        :param str name: The name of the process.
        :param qi::uint32_t priority: The new priority of the process.
        :returns bool: 
        """
        return self.proxy.setProcessPriority(name, priority)

    @lazy_init
    def setRobotHeightOffset(self, heightOffset):
        """

        :param float heightOffset: Height Offset of the robot from the ground.
        :returns bool: 
        """
        return self.proxy.setRobotHeightOffset(heightOffset)

    @lazy_init
    def startScheduler(self):
        """

        :returns bool: 
        """
        return self.proxy.startScheduler()

    @lazy_init
    def stopScheduler(self):
        """

        :returns bool: 
        """
        return self.proxy.stopScheduler()

    @lazy_init
    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        return self.proxy.version()
