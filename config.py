import os


class Config:
    SOURCES_URL = 'http://newsapi.org/v2/top-headlines/sources?apiKey={}'
    ARTICLE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    CATEGORY_URL = 'https://newsapi.org/v2/'
    SEARCH_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    API_KEY = os.environ.get('API_KEY')
    
    @staticmethod
    def init_app(app):
        pass
    
    
class ProdConfig:
    
    
    pass
    
     
    
    
    
class DevConfig(Config):
    DEBUG=True
        
        
        
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
    
    
    
    