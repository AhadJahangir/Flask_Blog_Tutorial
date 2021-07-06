from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

#Sets fields (title, content and submit) for submitting blogpost on webpage
class PostForm(FlaskForm):
    title = StringField ("Title", validators = [DataRequired()])
    content = TextAreaField ("Content", validators = [DataRequired()])
    submit = SubmitField("Post")