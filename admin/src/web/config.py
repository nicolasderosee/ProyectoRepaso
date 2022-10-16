from os import environ

class Config(object):
    
    """Base configuration."""
    
    SECRET_KEY = "secret"
    DEBUG = False
    TESTING = False


class ProductionConfig(Config): #objetos que heredan de config
    """Production configuration."""
    pass


class DevelopmentConfig(Config):
    """Development configuration.""" 
    DEBUG = True


class TestingConfig(Config):
    """Testing configuration.""" 
    TESTING = True


config = {
 "development": DevelopmentConfig,
 "test": TestingConfig,
 "production": ProductionConfig,
}