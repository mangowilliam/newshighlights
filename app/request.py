
import urllib.request,json
from .source import Source
from .articles import Article

# Getting api key
api_key = None
# Getting the movie base url
base_url = None
base1_url=None

def configure_request(app):
    global api_key,base_url,base1_url
    api_key = app.config['SOURCE_API_KEY']
    base_url = app.config["SOURCE_API_BASE_URL"]
    base1_url = app.config["ARTICLE_API_BASE_URL"]
# Getting api key

# Getting the base urls


def get_sources(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(sources,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results


def process_results(sources_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain movie details

    Returns :
        source_results: A list of movie objects
    '''
    source_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        country = source_item.get('country')
        description = source_item.get('description')
        category = source_item.get('category')
        url= source_item.get("url")
        source_object = Source(id,name,country, description,category,url)
        source_results.append(source_object)

    return source_results


def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base1_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)


    return articles_results


def process_articles(articles_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain movie details

    Returns :
        source_results: A list of movie objects
    '''
    articles_results = []
    
    for article_item in articles_list:
        id = article_item.get('id')
        name = article_item.get("name")
        title = article_item.get('title')
        description = article_item.get('description')
        url =article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        if urlToImage:
            articles_object = Article(id,name,title, description,url,urlToImage,publishedAt)
            articles_results.append(articles_object)

    return articles_results

