#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/albodytemperatureproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


# To not instance network connections until we actually want to
# do a proxy call
def lazy_init(fn):
    def init_if_needed(self, *args, **kwargs):
        if not self.proxy:
            self.proxy = ALProxy("ALBodyTemperature")
        return fn(self, *args, **kwargs)
    # Preserve method name and docs
    init_if_needed.__name__ = fn.__name__
    init_if_needed.__doc__ = fn.__doc__
    return init_if_needed


class ALBodyTemperature(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALBodyTemperature")

    @lazy_init
    def areNotificationsEnabled(self):
        """Return true if notifications are active.

        :returns bool: Return True if notifications are active.
        """
        return self.proxy.areNotificationsEnabled()

    @lazy_init
    def getTemperatureDiagnosis(self):
        """The actual state of the temperature diagnosis.

        :returns AL::ALValue: Return the current temperature diagnosis.
        """
        return self.proxy.getTemperatureDiagnosis()

    @lazy_init
    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    @lazy_init
    def setEnableNotifications(self, enable):
        """Enables / Disables temperature notifications.

        :param bool enable: If True enable temperature notifications. If False disable temperature notifications.
        """
        return self.proxy.setEnableNotifications(enable)

    @lazy_init
    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        return self.proxy.version()
