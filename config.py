import os


class Config:
    SOURCE_URL = 'http://newsapi.org/v2/top-headlines/sources?apiKey={}'
    ARTICLE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    CATEGORY_URL = 'https://newsapi.org/v2/'
    SEARCH_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    API_KEY = os.environ.get('API_KEY')
    
    
class ProdConfig:
    SOURCE_URL = 'http://newsapi.org/v2/top-headlines/sources?apiKey={}'
    ARTICLE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    CATEGORY_URL = 'https://newsapi.org/v2/'
    SEARCH_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    API_KEY = os.environ.get('API_KEY')
    
    
    
    