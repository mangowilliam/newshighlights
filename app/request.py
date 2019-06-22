from app import app
import urllib.request,json
from .models import source

Source = source.Source
# Getting api key
api_key = app.config['SOURCE_API_KEY']
# Getting the source base url
base_url = app.config["SOURCE_API_BASE_URL"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['results']:
            source_results_list = get_sources_response['results']
            source_results = proces_results(source_results_list)


    return source_results


def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain movie details

    Returns :
        source_results: A list of movie objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        title = source_item.get('original_title')
        description = source_item.get('overview')
        image = source_item.get("urlToImage")
        publishedAt= source_item.get("publishedAt")
       

        if image:
            source_object = Source(id,title,description,image,publishedAt)
            source_results.append(source_object)

    return source_results