#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alchestbuttonproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


# To not instance network connections until we actually want to
# do a proxy call
def lazy_init(fn):
    def init_if_needed(self, *args, **kwargs):
        if not self.proxy:
            self.proxy = ALProxy("ALChestButton")
        return fn(self, *args, **kwargs)
    # Preserve method name and docs
    init_if_needed.__name__ = fn.__name__
    init_if_needed.__doc__ = fn.__doc__
    return init_if_needed


class ALChestButton(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALChestButton")

    @lazy_init
    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    @lazy_init
    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        return self.proxy.version()
