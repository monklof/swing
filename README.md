# Swing

Python's configuration switcher by an environment variable inspired by Common Lisp's [envy](https://github.com/fukamachi/envy)

## Description

Swing is a configuration manager for python app, it uses an environment variable to determine a configuration to use. It makes developer switching configurations between different situations quickly.

## Install

```bash
pip install swing
```

## Usage

Assuming that you want to use a database while developing, and use another database when running it in production enviroment, using swing, it's simple, only one step:

Just define your configurations in some place of your code, eg. `settings.py`: 

```python
from swing import ConfigBase

class DevelopmentConfig(ConfigBase):

    __confname__ = "development"
    
    DEBUG = True
    DB_CONNECTION = "mysql://username:password@ip:port/dev_db"

class ProductionConfig(ConfigBase):

    __confname__ = "production"

    DEBUG = False
    DB_CONNECTION = "mysql://username:password@ip:port/production_db"
```

And you can access the configurations where you need now, eg. `app.py`: 

```python
import settings # this makes the configuration known by Swing
from swing import config
print config.DB_CONNECTION
```

Now, you can now set the Envrioment Variable `APP_ENV`'s value to `"development"`, and swing will use the "development" configuration.

eg. in unix-like systems, you will get:
```bash
$ APP_ENV=development python app.py
mysql://username:password@ip:port/dev_db
```

while with `APP_ENV=production`:
```bash
$ APP_ENV=production python app.py
mysql://username:password@ip:port/production_db
```

that's swing :)

## Configurations

### General

You have to subclass the class `swing.ConfigBase` to declare a configuration, and the configuration's name can be defined through the class's  `__confname__` attribute. If you do not set the `__confname__`, Swing will take the configuarion as the default configuration.

Then you can control which configuration to use through the *Enviroment Variable*, and access the attributes of the configuration through `swing.config`

### The Enviroment Variable

By default, the *Environment Variable* Swing used to control which configuration to use is `APP_ENV`. You can change it through `swing.set_env_var(the_new_enviroment_var)`.

`swing.get_env_var()` to get current *Enviroment Variable*

### Common Configurations

You can define some common configuration sharing by multiple configurations by just following the inheritance of python class, eg:

```python
from swing import ConfigBase
class CommonConfig(ConfigBase):

    SOME_COMMEN_SETTING = "some commen setting"

class DevelopmentConfig(CommonConfig):

    __confname__ = "development"
    
    DEBUG = True
    DB_CONNECTION = "mysql://username:password@ip:port/dev_db"

class ProductionConfig(CommonConfig):

    __confname__ = "production"

    DEBUG = False
    DB_CONNECTION = "mysql://username:password@ip:port/production_db"
```

## API

### ConfigBase

```class swing.ConfigBase```
> The super class used to define a configuration

>  - `__confname__` - the configuration name, "default" if not declared

### config

```python
swing.config
```
> This object points to the current configuration, you can access to the configuraton by accessing the object's attribute

### switch_config

```python
def switch_config(confname)
```
> switch to a the configuration the confname points
> - `confname` - the configuration the you want to use

### refresh_config

```python
def refresh_config()
```
> refresh the current configuration according to the current Eviroment Variable

### clear_config

```python
def clear_config()
```
> clear all configuration that defined yet

### set_env_var

```python
def set_env_var(env_var)
```
> set the Enviroment Variable that swing used to determine which configuration to use
> - `env_var` - the Enviroment Variable to use

### get_env_var

```python
def get_env_var()
```
> get the current Enviroment Variable


## Author

* Monklof (monklof@gmail.com)

## License

MIT

