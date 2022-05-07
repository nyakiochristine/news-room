

from flask import render_template
import flask
from . import main

@main.route('/')
def index():
    title = 'NewsRoom'






@main.route('/news/<word>')
def search(word):
    word_list =word.split("")
    word_format ="+" .join (word_list)
    searched_word = word_format.split
    title = flask; 'Results for {word}'
    return render_template('search.html',news=searched_word,title=title)