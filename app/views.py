from app import app
from .requests import get_news,get_news,search_news
from flask import render_template,request,redirect,url_for

    # Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    trending_news = get_news('trending')
    highlights_news = get_news('highlights')
    live_news = get_news('live')

    title = 'Home - You can view the latest news'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title = title, popular = trending_news, highlights = highlights_news, live = live_news )