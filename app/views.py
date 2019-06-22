from flask import render_template
from app import app

#views
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Home - All news around the globe"
    return render_template('index.html', title = title)

@app.route('/source/<source_id>')
def source(source_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('source.html',id = source_id)