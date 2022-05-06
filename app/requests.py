import urllib.request,json
from .models import Articles,Sources


apikey =None

BASE_SOURCE_URL = None
BASE_ARTICLES_URL = None
BASE_CATEGORY_URL = None
BASE_SEARCH_URL = None


def configure_request(app):
    global api_key,BASE_SOURCE_URL,BASE_ARTICLES_URL,BASE_CATEGORY_,BASE_SEARCH_URL
    api_key = app.config('API_KEY')
    BASE_SOURCE_URL = app.config['SOURCE_URL']
    BASE_ARTICLES_URL = app.config['ARTICLE_URL']
    BASE_CATEGORY_URL = app.config['CATEGORY_URL']
    BASE_SEARCH_URL= app.config ['SEARCH_URL']
    
    
def search_news(word):
    search_news_url = BASE_SEARCH_URL.format(word,api_key)
    with urllib.request.urlopen(search_news_url) as search_news:
        search_news_info= search_news.read()
        search_news_info_dict = json.loads(search_news_info)
        
        
        search_news_results= None
        
        if search_news_info_dict['articles']
            search_news_list = search_news_info_dict['articles']
            search_news_results = (search_news_list)


    return search_news_results
