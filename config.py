class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'you-will-never-guess'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
