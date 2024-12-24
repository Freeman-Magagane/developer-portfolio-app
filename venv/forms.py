from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('developer', 'Developer'), ('employer', 'Employer')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class DeveloperProfileForm(FlaskForm):
    github_link = StringField('GitHub Link', validators=[DataRequired()])
    portfolio_description = TextAreaField('Portfolio Description.Describe the projects you have been involved in')
    submit = SubmitField('Save Profile')

class EmployerProfileForm(FlaskForm):
    project_name = StringField('project name', validators=[DataRequired()])
    industry = StringField('Industry')
    submit = SubmitField('Save Profile')


class DeveloperSocialMedia(FlaskForm):
    linkedin = StringField('GitHub Link', validators=[DataRequired()])
    instagram =StringField('instagram handle', validators=[DataRequired()])
    facebook = StringField('facebook profile', validators=[DataRequired()])
    submit = SubmitField('Save social media')