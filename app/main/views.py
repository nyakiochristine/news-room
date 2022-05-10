

from flask import render_template, request,redirect, url_for
import flask
from . import main
from ..requests import get_sources,get_articles, get_articles_category

@main.route('/')
def index():
    title = 'NewsRoom'
    sources = get_sources
    search_news =request.args.get('news-query')
    if search_news :
        return redirect(url_for('.search',word=search_news))
    else :return render_template('index.html',title=title,sources=sources)
    
@main.route('/news/<id>')
def articles(id):
    title = "Article-News"
    articles = get_articles(id)
    return render_template('articles.html', title=title, articles=articles)

@main.route('/sports/')
def sports():
    title = "Sports Highlights"
    articles = get_articles_category('sports')
    return render_template('sports.html', title=title, articles=articles)

@main.route('/business/')
def business():
    title = "Business Highlights"
    articles = get_articles_category('business')
    return render_template('business.html', title=title, articles=articles)

@main.route('/technology')
def technology():
    title = "Technology Highlights"
    articles = get_articles_category('technology')
    return render_template('technology.html', title=title, articles=articles)

     






@main.route('/news/<word>')
def search(word):
    word_list =word.split("")
    word_format ="+" .join (word_list)
    searched_word = word_format.split
    title = flask; 'Results for {word}'
    return render_template('search.html',news=searched_word,title=title)

