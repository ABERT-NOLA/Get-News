#from app import app
import urllib.request,json
#from .main import main
from .models import Sources,Articles

#News = news.News
# Getting api key
api_key = None
# Getting the news base url
base_url = None
def configure_requests(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config ['NEWS_API_BASE_URL']

def get_news(category):

    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results
def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category, api_key)
    print(get_sources_url)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results
def process_results(news_list):
    
    sources_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        
        news_object = Sources(id,name,description,url,category,language,country)
        sources_results.append(news_object)

    return sources_results

def search_news(news_name):

    search_news_url = 'https://newsapi.org/v2/top-headlines?sources=%s&apiKey=%s'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

    search_news_results = None

    if search_news_response['results']:
        search_news_list = search_news_response['results']
        search_news_results = process_results(search_news_list)


    return search_news_results

def process_article_response(articles):
    results_list = []

    for article_item in articles:
        author = article_item.get('author')
        title = article_item.get('title')
        desc = article_item.get('description')
        image = article_item.get('urlToImage')
        url = article_item.get('url')
        source = article_item.get('source')['name']

        article_object = Article(author, title, desc, image, url, source)
        results_list.append(article_object)
    return results_list