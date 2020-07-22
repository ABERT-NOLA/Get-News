#from app import app
import urllib.request,json
#from .main import main


News = news.News
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
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
    def process_results(news_list):
        news_results = []
        for news_item in news_list:
            id = news_item.get('id')
            title = news_item.get('original_title')
            overview = news_item.get('overview')
            poster = news_item.get('poster_path')
            vote_average = news_item.get('vote_average')
            vote_count = news_item.get('vote_count')

        if poster:
          news_object = news(id,title,overview,poster,vote_average,vote_count)
          news_results.append(news_object)

        return news_results

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