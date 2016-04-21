# Swing

Configuration switcher by an environment variable inspired by Common Lisp's [envy](https://github.com/fukamachi/envy)

## Usage

Assuming that you have to access to a debug database other then the online one when in development environment.

Use swing, it's simple:

1. config the configuration settings in your `settings.py`
2. access the configuration through `swing.config` in your "foo.py"
3. start the application with Enviroment Varialble `APP_ENV=development`, for example in unix:

    ```
    $ APP_ENV=development python foo.py
    ``` 

### config the configuration


settings.py:

```python
from swing import Config, config

class DevelopmentConfig(Config):

    __confname__ = "development"
    
    DEBUG = True
    DB_CONNECTION = "mysql://username:password@ip:port/dev_db"

class ProductionConfig(Config):

    __confname__ = "production"

    DEBUG = False
    DB_CONNECTION = "mysql://username:password@ip:port/production_db"

```

### access to configuration

foo.py

```python
import settings
from swing import config

print config.DB_CONNECTION
```

### run it!

```bash
$ APP_ENV=development python foo.py
```

## Description

## Configuration

### Normal configurations

### Merging

### Common configurations

### Accessing to configuration

## Tips

## Author

* Monklof (monklof@gmail.com)

## License

MIT

