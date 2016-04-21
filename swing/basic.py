import os

# store all the configurations found
configurations = {}
# the enviroment varaible used to specify which config to use
env_name = "APP_ENV"

class metacls(type):
    '''meta class for listening the config class's definition'''
    def __new__(mcs, name, bases, dict):
        the_class =  type.__new__(mcs, name, bases, dict)

        # jump it when if it is the Base `ConfigBase` class
        if dict.get("__is_base_confclass__"):
            return the_class
        # set confname to "default" when not set
        if not dict.get("__confname__"):
            dict["__confname__"] = "default"
        global configurations

        configurations[dict["__confname__"]] = the_class
        refresh_config()
        return the_class

class ConfigBase(object):
    
    __metaclass__ = metacls
    __is_base_confclass__ = True
    

class ClassProxy(object):

    def __init__(self, cls):
        self.__dict__['cls'] = cls

    def set_class(self, cls):
        self.__dict__['cls'] = cls

    def __getattr__(self, name):
        if name in self.__dict__:
            return getattr(self, name)
        else:
            if self.cls is _DefaultConfig:
                raise LookupError("no configuration found (tips: have you once imported the configuration file? )")
            try:
                return getattr(self.cls, name)
            except AttributeError as e:
                raise AttributeError("the '%s' configuration does has no config named '%s'" % (
                    self.cls.__confname__, name))

    def __setattr__(self, name, value):
        if name in self.__dict__:
            return setattr(self, name, value)
        else:
            return setattr(self.cls, name, value)


class _DefaultConfig(object):
    __confname__ = "default"

def default_config():
    return ClassProxy(_DefaultConfig)

config = default_config()

def set_env_var(env_var):
    '''set the enviroment variable name
    swing will use the env value of `env_var` to figure out
    which configuration should be used
    '''
    global env_name
    env_name = env_var

def get_env_var():
    return env_name

def switch_config(confname):
    if confname not in configurations:
        raise ValueError("configuration: %s not found" % confname)
    global config
    config.set_class(configurations[confname])

def refresh_config():
    confname = os.environ.get(env_name, "default")
    if confname in configurations:
        switch_config(confname)
    
def clear_config():
    '''clear all configurations and reset the current config'''
    global configurations
    global config
    configurations.clear()
    config.set_class(_DefaultConfig)
