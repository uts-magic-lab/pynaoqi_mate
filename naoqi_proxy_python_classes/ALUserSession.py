#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alusersessionproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


# To not instance network connections until we actually want to
# do a proxy call
def lazy_init(fn):
    def init_if_needed(self, *args, **kwargs):
        if not self.proxy:
            self.proxy = ALProxy("ALUserSession")
        return fn(self, *args, **kwargs)
    # Preserve method name and docs
    init_if_needed.__name__ = fn.__name__
    init_if_needed.__doc__ = fn.__doc__
    return init_if_needed


class ALUserSession(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALUserSession")

    @lazy_init
    def areUserSessionsOpen(self, user_list):
        """Check if users have an open session.

        :param std::vector<int> user_list: A list of int IDs of each user to check.
        :returns bool: A bool, true if all users have open sessions.
        """
        return self.proxy.areUserSessionsOpen(user_list)

    @lazy_init
    def doUsersExist(self, user_list):
        """Check if users exist in db.

        :param std::vector<int> user_list: A list of int ID of the users to check.
        :returns bool: A bool, true if all users exist.
        """
        return self.proxy.doUsersExist(user_list)

    @lazy_init
    def doesBindingSourceExist(self, binding_name):
        """Query if a particular has been applied to UserSession

        :param str binding_name: The string name of the binding source.
        :returns bool: A bool, true if a binding source exists.
        """
        return self.proxy.doesBindingSourceExist(binding_name)

    @lazy_init
    def doesUserDataSourceExist(self, source_name):
        """Check if a data source has been registered.

        :param str source_name: The string name of the data source.
        :returns bool: A bool, true if the source has been registered
        """
        return self.proxy.doesUserDataSourceExist(source_name)

    @lazy_init
    def findUsersWithBinding(self, binding_name, binding_value):
        """Get the sources a user is bound to.

        :param str binding_name: The string name of the binding source.
        :param str binding_value: The string ID of the user at the binding source.
        :returns std::vector<int>: The int IDs of the users with the passed binding_value.
        """
        return self.proxy.findUsersWithBinding(binding_name, binding_value)

    @lazy_init
    def getBindingSources(self):
        """The list of binding sources  that have been applied to UserSession

        :returns std::vector<std::string>: A list of strings, one for each binding source.
        """
        return self.proxy.getBindingSources()

    @lazy_init
    def getFocusedUser(self):
        """Get which user has the robot's focus.

        :returns int: The int ID of the focused user. -1 if no focused user.
        """
        return self.proxy.getFocusedUser()

    @lazy_init
    def getNumUsers(self):
        """Get the count of users in db.

        :returns int: An int of how many users exist
        """
        return self.proxy.getNumUsers()

    @lazy_init
    def getOpenUserSessions(self):
        """Get which users have an open session.

        :returns std::vector<int>: A list of int IDs of each user with an open session.
        """
        return self.proxy.getOpenUserSessions()

    @lazy_init
    def getUserBinding(self, uid, binding_name):
        """Get the a specific source a user is bound to.

        :param int uid: The int ID of the user.
        :param str binding_name: The string name of the binding source.
        :returns str: The string value of the binding ID for the user.
        """
        return self.proxy.getUserBinding(uid, binding_name)

    @lazy_init
    def getUserBindings(self, uid):
        """Get the sources a user is bound to.

        :param int uid: The int ID of the user.
        :returns std::map<std::string , std::string>: A map of string binding names and their string values.
        """
        return self.proxy.getUserBindings(uid)

    @lazy_init
    def getUserData(self, uid, data_name):
        """Get some data about a user.  Will throw if it does not exist

        :param int uid: The int ID of the user whose data to get.
        :param str data_name: The key of the data to get.
        :returns std::map<std::string , AL::ALValue>: A map keyed by source_name of ALValues of the data.
        """
        return self.proxy.getUserData(uid, data_name)

    @lazy_init
    def getUserData2(self, uid, data_name, source_name):
        """Get some data about a user.  Will throw if it does not exist

        :param int uid: The int ID of the user whose data to get.
        :param str data_name: The key of the data to get.
        :param str source_name: The string name of the data source.
        :returns AL::ALValue: ALValue of the data.
        """
        return self.proxy.getUserData(uid, data_name, source_name)

    @lazy_init
    def getUserDataSources(self):
        """Check what data sources have been registered.

        :returns std::vector<std::string>: A list of strings of each registered data source.
        """
        return self.proxy.getUserDataSources()

    @lazy_init
    def getUserList(self):
        """Get a full list of the users.

        :returns std::vector<int>: A list of int user IDs.
        """
        return self.proxy.getUserList()

    @lazy_init
    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    @lazy_init
    def setUserData(self, uid, data_name, source_name, data):
        """Set some data about a user.  Will throw if user does not exist

        :param int uid: The int ID of the user whose data to set.
        :param str data_name: The key of the data to set.
        :param str source_name: The string name of the data source.
        :param AL::ALValue data: ALValue of the data.
        """
        return self.proxy.setUserData(uid, data_name, source_name, data)

    @lazy_init
    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        return self.proxy.version()
