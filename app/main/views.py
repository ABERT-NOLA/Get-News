from . import main
from ..requests import get_news, search_news,get_sources
from flask import render_template,request,redirect,url_for

    # Views
@main.route('/')
def index():
    '''
    view root page function that returns the index the page and its data
    '''
    sources = get_sources('business')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    title = "News Highlighter"

    print(entertainment_sources)
    return render_template('index.html', title = title, sources = sources, sports_sources = sports_sources, technology = technology_sources, entertainment_sources = entertainment_sources)
@main.route('/sources/<id>')
def articles(id):
    '''
    view articles page
    '''
    articles = get_articles(id)
    title = f'NH | {id}'

    return render_template('articles.html', title = title, articles = articles)
