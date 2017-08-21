from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms import validators

from ..utils.validators import Unique


class SigninForm(Form):
    email = StringField('Email', [validators.DataRequired(),
                                  validators.Email(),
                                  validators.Length(min=6, max=50),
                                  Unique()])
    password = PasswordField("Password", [validators.DataRequired()])
