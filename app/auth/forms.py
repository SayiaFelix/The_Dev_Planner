from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Email Address:',validators=[DataRequired(),Email()])
    author = StringField('Enter Name:',validators = [DataRequired()])
    password = PasswordField('Password:',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password:',validators = [DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('Email exists already.')

    def validate_author(self,data_field):
        if User.query.filter_by(author = data_field.data).first():
            raise ValidationError('Author name is taken already.')

class LoginForm(FlaskForm):
    email = StringField('Email Address:',validators=[DataRequired(),Email()])
    password = PasswordField('Password:',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')