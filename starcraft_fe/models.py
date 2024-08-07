from datetime import datetime
from itsdangerous import URLSafeTimedSerializer as Serializer
from starcraft_fe import db, login_manager
from flask import current_app
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.types import PickleType

@login_manager.user_loader
def load_user(user_id):
    return Starcraft_User.query.get(int(user_id))

class Starcraft_User(db.Model, UserMixin):
    __tablename__ = 'starcraft_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    role = db.Column(db.String(20), nullable=False, default='user')

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return Starcraft_User.query.get(user_id)

    def __repr__(self):
        return f"Starcraft_User('{self.username}', '{self.email}', '{self.image_file}', '{self.role}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(200), nullable=False)
    races = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('starcraft_user.id'), nullable=False)
    subtitle = db.Column(db.String(64), nullable=False)
    levels = db.Column(db.String(50), nullable=False) 
    youtube = db.Column(db.String(200), nullable=True)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', '{self.races}', '{self.levels}', '{self.category}')"