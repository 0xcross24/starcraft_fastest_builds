# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor
from flask_migrate import Migrate
from flask_admin import Admin

app = Flask(__name__)

app.config['SECRET_KEY'] = '13059654fc05573ad35f44a5e0b51d68'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///build.db'



db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
ckeditor = CKEditor(app)
migrate = Migrate(app, db)
admin = Admin(app, name='My Admin Panel', template_mode='bootstrap5')



from starcraft_fe.users.routes import users
from starcraft_fe.posts.routes import posts
from starcraft_fe.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)