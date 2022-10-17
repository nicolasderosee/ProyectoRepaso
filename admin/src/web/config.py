from os import environ #obtengo var de entorno

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
    DB_USER = "postgres"
    DB_PASS = "postgres"
    DB_HOST = "localhost"
    DB_NAME = "ProyectoSoftware"
    SQLALCHEMY_TRACK_MODIFICATION = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )



class TestingConfig(Config):
    """Testing configuration.""" 
    TESTING = True


config = {
 "development": DevelopmentConfig,
 "test": TestingConfig,
 "production": ProductionConfig,
}