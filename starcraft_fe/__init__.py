# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor
from flask_migrate import Migrate
from flask_caching import Cache
from starcraft_fe.config import Config

cache = Cache()
mail = Mail()

#app.config['SECRET_KEY'] = '13059654fc05573ad35f44a5e0b51d68'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///build.db'
#app.config['CKEDITOR_PKG_TYPE'] = 'full-all'
#app.config['allowedContent'] = True
#app.config['CACHE_TYPE'] = 'simple'

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
ckeditor = CKEditor()
migrate = Migrate()

#app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
#app.config['MAIL_PORT'] = 587
#app.config['MAIL_USE_TLS'] = True
#app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
#app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    cache.init_app(app)
    mail.init_app(app)
    ckeditor.init_app(app)
    migrate.init_app(app, db)

    from starcraft_fe.users.routes import users
    from starcraft_fe.posts.routes import posts
    from starcraft_fe.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    from starcraft_fe.admin import init_admin
    init_admin(app)  # Initialize Admin

    return app
