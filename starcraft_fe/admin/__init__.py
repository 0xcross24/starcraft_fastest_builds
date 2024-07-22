# starcraft_fe/admin/__init__.py
from flask import Blueprint, redirect, url_for, request
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, login_required
from flask import redirect, url_for, request
from starcraft_fe import db
from starcraft_fe.models import Starcraft_User, Post

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        if not current_user.is_authenticated or current_user.role != 'admin':
            return redirect(url_for('main.index'))
        return super(MyAdminIndexView, self).index()

class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == 'admin'

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('users.login', next=request.url))

def init_admin(app):
    admin = Admin(app, name='Admin Dashboard', template_mode='bootstrap4', index_view=MyAdminIndexView())
    admin.add_view(SecureModelView(Starcraft_User, db.session))
    admin.add_view(SecureModelView(Post, db.session))
    return admin