from datetime import datetime
from starcraft_fe import db, login_manager
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.types import PickleType

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    role = db.Column(db.String(20), nullable=False, default='user')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}', '{self.role}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(200), nullable=False)
    races = db.Column(PickleType, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subtitle = db.Column(db.String(64), nullable=False)
    levels = db.Column(PickleType, nullable=False)
    youtube = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', '{self.races}', '{self.levels}')"