from flask_admin.contrib.sqla import ModelView

class UserAdmin(ModelView):
    column_list = ('username', 'email', 'role')
    column_labels = {'username': 'Username', 'email': 'Email Address', 'role': 'Role'}
    column_filters = ('username', 'email', 'role.name')

class PostAdmin(ModelView):
    column_list = ('title', 'author', 'content')
    column_labels = {'title': 'Post Title', 'author': 'Author', 'content': 'Content'}
    column_filters = ('title', 'author.username')