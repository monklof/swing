import os
from nose.tools import with_setup
from swing import ConfigBase, config, switch_config, refresh_config, clear_config, get_env_var, set_env_var

def setup_func():
    class DefaultConfig(ConfigBase):
        DEBUG = None
    
    class DevelopmentConfig(ConfigBase):
        __confname__ = "development"
        DEBUG = True

    class ProductionConfig(ConfigBase):
        __confname__ = "production"
        DEBUG = False

def teardown_func():
    if get_env_var() in os.environ:
        del os.environ[get_env_var()]
    clear_config()
    
@with_setup(lambda : None, teardown_func)
def test_access_with_no_configuration():
    try:
        config.DEBUG
    except LookupError:
        return

    assert False

@with_setup(setup_func, teardown_func)
def test_define_default_configuration():
    assert config.DEBUG is None

@with_setup(setup_func, teardown_func)
def test_define_multi_configurations():
    os.environ[get_env_var()] = "development"
    refresh_config()
    assert config.DEBUG is True
    os.environ[get_env_var()] = "production"
    refresh_config()
    assert config.DEBUG is False

def test_configuration_not_found():
    os.environ[get_env_var()] = "no such conf"
    class DevelopmentConfig(ConfigBase):
        __confname__ = "development"
        TEST = True
    try:
        config.TEST
    except LookupError:
        teardown_func()
        return
    teardown_func()
    assert False

@with_setup(setup_func, teardown_func)
def test_attribute_not_found():
    os.environ[get_env_var()] = "development"
    refresh_config()
    try:
        config.DBURL
    except AttributeError:
        return
    assert False

@with_setup(setup_func, teardown_func)
def test_set_env_var():
    import os
    set_env_var("SWING_ENV")
    assert get_env_var() == "SWING_ENV"
    os.environ["SWING_ENV"] = "development"
    refresh_config()
    assert config.DEBUG is True
    os.environ["SWING_ENV"] = "production"
    refresh_config()
    assert config.DEBUG is False

@with_setup(setup_func, teardown_func)
def test_switch_config():
    assert config.DEBUG is None
    switch_config("development")
    assert config.DEBUG is True
    
