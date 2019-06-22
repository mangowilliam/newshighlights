from flask import render_template
from app import app
from .request import get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     # Getting sources
    news_sources = get_sources('sources')
    title = "Home - All news around the globe"
    return render_template('index.html', title = title,sources=news_sources)

@app.route('/source/<source_id>')
def source(source_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('source.html',id = source_id)