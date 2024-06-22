# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = '13059654fc05573ad35f44a5e0b51d68'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///build.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
ckeditor = CKEditor(app)
migrate = Migrate(app, db)

from starcraft_fe import routes
