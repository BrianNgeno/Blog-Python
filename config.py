import os

class Config():
    '''
    parent class config
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bknngeno:123@localhost/pitches'
    UPLOAD_PHOTOS_DEST ='app/static/photos'
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    pass

config_options = {
    'production':ProdConfig,
    'development':DevConfig,
    'test':TestConfig
}