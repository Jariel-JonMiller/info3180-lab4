from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    fileImg = FileField('Image', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])