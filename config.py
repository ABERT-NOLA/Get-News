import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL='https://newsapi.org/v2/sources?country=us&category={}&apiKey={}'
    NEWS_API_KEY='58604a94b3cc48da8be4ffa0d02c96cb'
    SECRET_KEY=os.environ.get('SECRET_KEY')



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}