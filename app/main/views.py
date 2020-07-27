from . import main
from ..requests import get_news, search_news,get_sources,articles_source
from flask import render_template,request,redirect,url_for
from ..models import Sources

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
@main.route('/sources/<sources>')
def articles(sources):
    '''
    view articles page
    '''
    articles = process_article_response(sources)
    title = f'NH | {sources}'

    return render_template('articles.html', title = title, articles = articles)
@main.route('/articles/<id>')
def articleSearch(id):
    all_articles = articles_source(id)
    source = id
    return render_template('articles.html', articles = all_articles, source = source) 