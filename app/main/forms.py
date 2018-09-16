from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField('Blog title',validators=[Required()])
    content = TextAreaField('Your Blog.')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Blog comment', validators=[Required()])
    submit = SubmitField('Submit')