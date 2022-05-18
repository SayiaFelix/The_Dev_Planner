from flask import render_template
from flask import render_template,request,redirect,url_for,abort, flash
from flask_login import login_required,current_user
from ..email import mail_message
from ..models import *
from . import main
from .. import db,photos
from .forms import UpdateProfile,SubscriberForm

@main.route('/')
def index():
    '''
    my index page
    return
    '''
  
    title= "The Dev Planner Hub ::"
    return render_template('index.html',title=title)



@main.route('/subscribe', methods=['GET','POST'])
def subscriber():

    subscriber_form = SubscriberForm()
  

    if subscriber_form.validate_on_submit():

        subscriber= Subscriber(email=subscriber_form.email.data,name = subscriber_form.name.data)

        db.session.add(subscriber)
        db.session.commit()

        mail_message("Hello, Welcome To The Dev Planner Hub.","email/welcome_subscriber",subscriber.email,subscriber=subscriber)
       
        title = "The Dev Planner Hub:"
        return render_template('index.html',title=title)

    
  

    return render_template('subscribe.html',subscriber_form=subscriber_form)