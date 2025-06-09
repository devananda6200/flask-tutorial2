from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, RadioField, SelectField,SubmitField

from wtforms import validators, ValidationError

class ContactForm(FlaskForm):
    name = StringField("Name of Student",[validators.  DataRequired("Please enter your name!")])
    Gender =  RadioField('Gender', choices = [('M','Male'),('F','Female')])
    Address = TextAreaField("Address")
    email=StringField("Email",[validators.DataRequired("Please enter your email address"),validators.Email("Please enter correct email address")]) 
    age = IntegerField("age")
    language=SelectField('Language',choices=[('cpp','C++'),('py','Python')]) 
    submit=SubmitField("Send")