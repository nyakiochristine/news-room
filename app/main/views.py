

from flask import render_template, request,redirect, url_for
import flask
from app import main
from ..requests import get_sources,get_news_articles, search_news

@main.route('/')
def index():
    title = 'NewsRoom'
    sources = get_sources
    search_news =request.args.get('news-query')
    if search_news :
        return redirect(url_for('.search',word=search_news))
    else :return render_template('index.html',title=title,sources=sources)
    
    






@main.route('/news/<word>')
def search(word):
    word_list =word.split("")
    word_format ="+" .join (word_list)
    searched_word = word_format.split
    title = flask; 'Results for {word}'
    return render_template('search.html',news=searched_word,title=title)