from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Length, Email,Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


#class NameForm(Form):
    #name = StringField('What is your name?', validators=[Required()])
    #submit = SubmitField('Submit')


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required])
    remember_me = BooleanField('keep me login in')
    submit = SubmitField('login')


class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    username = StringField('Username',validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-za-z0-9_.]*$', 0,
                                       'Username must have only letters,'
                                       'numbers,dots or underscores')])
    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message='passwords must match.')])
    password2 = PasswordField('confirm password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email already registered')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username already in use')