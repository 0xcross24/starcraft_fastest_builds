from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, Optional

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    races = SelectMultipleField('Races', validators=[DataRequired()], choices=[
        ('Zerg', 'Zerg'),
        ('Protoss', 'Protoss'),
        ('Terran', 'Terran'),
    ])
    levels = SelectMultipleField('Levels', validators=[DataRequired()], choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    ])
    category = SelectMultipleField('Categories', validators=[DataRequired()], choices=[
        ('1v1', '1v1'),
        ('3v3', '3v3'),
        ('In-House', 'In-House'),
    ])
    content = TextAreaField('Content', validators=[DataRequired()])
    youtube = StringField('Youtube', validators=[Optional()])
    submit = SubmitField('Post')