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

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
ckeditor = CKEditor()
migrate = Migrate()


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
