from flask import Blueprint, render_template, request, redirect, url_for
from starcraft_fe import cache

main = Blueprint('main', __name__)

@cache.cached(timeout=50)
@main.route('/')
def index():
    return render_template('index.html')

@cache.cached(timeout=50)
@main.route('/<string:category>', endpoint='category')
def category(category):
    return render_template('race.html', category=category)

@main.route('/error')
def error():
    return render_template('error.html')

@main.route("/about")
def about():
    return render_template('about.html')

@main.route('/donation')
def donation():
    return render_template('donation.html')

@main.route('/test')
def test():
    return render_template('test.html')