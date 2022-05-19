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

@main.route('/dashboard')
@login_required
def dashboard():
    '''
    return              
    '''
  
    title= "Dashboard ::"
    return render_template('Dashboard.html',title=title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(author = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(author = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.author))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(author = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

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