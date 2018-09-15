from flask import render_template,redirect,url_for,abort,request
from . import main
from flask_login import login_required

@main.route('/')
def index():
    '''
    view root page function that returns the index page
    '''
    title = 'Home - Welcome to The Best Blog Site Worldwide You Think of It We help share It.'

    return render_template('index.html',title=title)

