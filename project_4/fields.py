from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired


class RegistrationFields(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    surname = StringField('Surname: ', validators=[DataRequired()])
    email = EmailField('e-mail: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat password: ', validators=[DataRequired()])