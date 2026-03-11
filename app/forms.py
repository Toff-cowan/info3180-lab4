from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class UploadForm(FlaskForm):
    """Form for uploading image files (jpg, png only)."""
    upload = FileField(
        'Image',
        validators=[
            FileRequired(message='Please select a file to upload.'),
            FileAllowed(['jpg', 'jpeg', 'png'], 'Only JPG and PNG images are allowed.')
        ]
    )