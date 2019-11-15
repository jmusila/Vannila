import os


class Config(object):
    SECRET_KEY = os.urandom(32)
    # Grabs the folder where the script runs.
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Enable debug mode.
    DEBUG = False

class DevelopmentConfig(Config):
    """ Development configurations """
    DEBUG = True

class ProductionConfig(Config):
    """ Production configurations """
    DEBUG = True

class TestingConfig(Config):
    """ Testing configurations """
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    """ Staging configurations """
    DEBUG = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'staging': StagingConfig
}
