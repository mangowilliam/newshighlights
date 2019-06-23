from flask import render_template,request,redirect
from app import app
from .request import get_sources,get_articles

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

@app.route('/articles/<source_name>')
def articles(source_name):

    '''
    View movie page function that returns the movie details page and its data
    '''
    title= f"{source_name}"
    articles = get_articles(source_name)
  
    return render_template('articles.html',source_name=articles,title=title)