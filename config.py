import os
class Config:
    '''
    General configuration parent class
    '''
    
    SOURCE_API_BASE_URL ='https://newsapi.org/v1/{}?api_key={}'
    ARTICLE_API_BASE_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SOURCE_API_KEY= os.environ.get(' SOURCE_API_KEY')



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}