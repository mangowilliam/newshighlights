from flask import render_template
from app import app
from .request import get_sources

#views
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     # Getting popular movie
    sources = get_sources('sources')
    print(sources)
    title = "Home - All news around the globe"
    return render_template('index.html', title = title,sources=sources)

@app.route('/source/<source_id>')
def source(source_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('source.html',id = source_id)