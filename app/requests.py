import urllib.request,json
from .models import Articles,Sources


apikey =None

BASE_SOURCES_URL = None
BASE_ARTICLES_URL = None
BASE_CATEGORY_URL = None
BASE_SEARCH_URL = None


def configure_request(app):
    global api_key,BASE_SOURCES_URL,BASE_ARTICLES_URL,BASE_CATEGORY_,BASE_SEARCH_URL
    BASE_SOURCES_URL = app.config['SOURCES_URL']
    BASE_ARTICLES_URL = app.config['ARTICLE_URL']
    BASE_CATEGORY_URL = app.config['CATEGORY_URL']
    BASE_SEARCH_URL= app.config ['SEARCH_URL']
def get_sources():
    news_source_url = BASE_SOURCES_URL.format(api_key)
    with urllib.request.urlopen(news_source_url) as news_source:
        source_info = news_source.read()
        source_info_dict = json.loads(source_info)
        sources_results = None
        
        if source_info_dict['sources']:
            sources_list= source_info_dict['sources']
            sources_results = process_sources(sources_list)
        return sources_results
    
    
def process_sources(sources):
    sources_list = []
    for source in sources:
        id = source['id']
        name = source['name']
        description = source['description']
        url = source['url']
        country = source['country']
        language = source['language']
        category = source['category']
        
        if url:
            source_object = Sources(id, name, description, url, country, language, category)
            sources_list.append(source_object)
        return sources_list
    
    
def get_articles(id):
    articles_url = BASE_ARTICLES_URL.format(id,api_key)
    with urllib.request.urlopen(articles_url) as articles:
        articles_info = articles.read()
        articles_info_dict = json.loads(articles_info)
        
        articles_results = None
        
        if articles_info_dict['articles']:
            articles_list = articles_info_dict['articles']
            articles_results = process_articles(articles_list)
        return articles_results
    
    
def process_articles(info):
    articles_results = []
    for article in info['articles']:
        image = article['urlToImage']
        description = article['description']
        time= article['publishedAt']
        url = article['url']
        title = article['title']
        author = article['author']
        
        if time:
            articles_object = Articles(image, description,time,url,title,author)
            articles_results.append(articles_object)
        
def get_articles_category(category):
    category_url = BASE_CATEGORY_URL.format(category,api_key)
    with urllib.request.urlopen(category_url) as category_news:
        category_info = category_news.read()
        category_info_dict =json.loads(category_info)
        category_results = None
        
        if category_info_dict['articles']:
            category_list = category_info_dict['articles']
            category_results = process_articles(category_list)
        return category_results
    
    
        
        
    
    
    

    
    
    
def search_news(word):
    search_news_url = BASE_SEARCH_URL.format(word,api_key)
    with urllib.request.urlopen(search_news_url) as search_news:
        search_news_info= search_news.read()
        search_news_info_dict = json.loads(search_news_info)
        
        
        search_news_results= None
        
        if search_news_info_dict['articles']:
            search_news_list = search_news_info_dict['articles']
            search_news_results = (search_news_list)


    return search_news_results
