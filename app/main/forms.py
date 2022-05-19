from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Add Your Bio ::',validators = [DataRequired()])
    submit = SubmitField('Upload')

class TaskForm(FlaskForm):
    name = StringField('Name ')
    date= StringField('Date ')
    description = TextAreaField('Description ')
    submit = SubmitField('Add ')

class WeeklyForm(FlaskForm):
    name = StringField('Name ')
    date= StringField('Date ')
    description = TextAreaField('Description ')
    category = SelectField('Day', choices=[('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thursday','Thursday'),('Friday','Friday'),('Saturday','Saturday')],validators=[DataRequired()])
    submit = SubmitField('Add ')

class SubscriberForm(FlaskForm):
    email = StringField('Email Address ::')
    name = StringField('Enter your name ::',validators = [DataRequired()])
    submit = SubmitField('Subscribe')