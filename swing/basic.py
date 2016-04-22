import os

# store all the configurations found
_configurations = {}
# the enviroment varaible used to specify which config to use
_env_name = "APP_ENV"
_default_confname = "default"

class metacls(type):
    '''meta class for listening the config class's definition'''
    def __new__(mcs, name, bases, dict):
        # jump it when if it is the Base `ConfigBase` class
        if dict.get("__is_base_confclass__"):
            return type.__new__(mcs, name, bases, dict)
        # set confname to _default_confname when not set
        if not dict.get("__confname__"):
            dict["__confname__"] = _default_confname
        the_class = type.__new__(mcs, name, bases, dict)
        global _configurations

        _configurations[dict["__confname__"]] = the_class
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
                raise LookupError("configuration<%s> not found" % _env_confname())
            try:
                return getattr(self.cls, name)
            except AttributeError as e:
                raise AttributeError("the configuration<%s> does has no attribute named '%s'" % (
                    self.cls.__confname__, name))

    def __setattr__(self, name, value):
        if name in self.__dict__:
            return setattr(self, name, value)
        else:
            return setattr(self.cls, name, value)


class _DefaultConfig(object):
    __confname__ = _default_confname

def default_config():
    return ClassProxy(_DefaultConfig)

config = default_config()

def set_env_var(env_var):
    '''set the enviroment variable name
    swing will use the env value of `env_var` to figure out
    which configuration should be used
    '''
    global _env_name
    _env_name = env_var

def get_env_var():
    return _env_name

def switch_config(confname):
    if confname not in _configurations:
        raise ValueError("configuration: %s not found" % confname)
    global config
    config.set_class(_configurations[confname])

def refresh_config():
    confname = _env_confname()
    if confname in _configurations:
        switch_config(confname)
    
def clear_config():
    '''clear all configurations and reset the current config'''
    global _configurations
    global config
    _configurations.clear()
    config.set_class(_DefaultConfig)


def _env_confname():
    return os.environ.get(_env_name, _default_confname)
