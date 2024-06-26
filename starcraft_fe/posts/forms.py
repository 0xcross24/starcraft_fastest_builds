from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired

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
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

