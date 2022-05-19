from unicodedata import category
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    author = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    task = db.relationship('Task', backref='author', lazy='dynamic')
    WeeklyTask = db.relationship('WeeklyTask', backref='author', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"{self.author}"


class Task(db.Model):
    __tablename__= 'task'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    def save_blog(self,task):
        db.session.add(task)
        db.session.commit()

    @classmethod
    def get_tasks(id):
        task = task.query.filter_by(name= name).all()
        return task

    def __repr__(self):
        return f"Task :: {self.id}',{self.name}',{self.description}')"

  
class WeeklyTask(db.Model):
    __tablename__= 'wtask'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    category = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    

    def save_blog(self,task):
        db.session.add(task)
        db.session.commit()

    @classmethod
    def get_tasks(id):
        task = task.query.filter_by(name = name).all()
        return task

    def __repr__(self):
        return f"Weekly Task :: {self.id}',{self.name}',{self.description}')"




class Subscriber(UserMixin, db.Model):
   __tablename__="subscribers"

   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(255))
   email = db.Column(db.String(255),unique = True,index = True)


   def save_subscriber(self):
       db.session.add(self)
       db.session.commit()

   @classmethod
   def get_subscribers(cls,id):
       return Subscriber.query.all()


   def __repr__(self):
       return f'User {self.email}'

