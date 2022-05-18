from flask import render_template, request, redirect, url_for, abort,flash
from . import main
from flask_login import login_required, current_user
from datetime import datetime


@main.route('/')
def index():
    '''
    '''
    return render_template('index.html')