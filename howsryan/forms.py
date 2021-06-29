from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=2)])
    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(), Length(min=2), EqualTo("password")])
    submit = SubmitField("Create Account")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=2)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class UpdateForm(FlaskForm):
    book_title = StringField("Title", validators=[DataRequired()])
    book_author = StringField("Author", validators=[DataRequired()])
    status = StringField("Status", validators=[DataRequired()])
    project = TextAreaField("Project", validators=[DataRequired()])
    submit = SubmitField("Update Books")
