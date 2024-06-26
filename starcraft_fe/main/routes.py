from flask import Blueprint, render_template, request


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/error')
def error():
    return render_template('404.html')


@main.route("/about")
def about():
    return render_template('about.html')

@main.route('/donation')
def donation():
    return render_template('donation.html')