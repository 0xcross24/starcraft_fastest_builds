from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from starcraft_fe import db
from starcraft_fe.posts.forms import PostForm
from starcraft_fe.models import Post

posts = Blueprint('posts', __name__)

@posts.route("/build/new", methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        level_format = form.levels.data[0].lower()
        race_format = form.races.data[0].lower()
        post = Post(title=form.title.data, subtitle=form.subtitle.data, races=race_format, levels=level_format, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index'))
    else:
        print(form.errors)  # Print out form validation errors
    return render_template('create.html', form=form, legend="New Post")

@posts.route('/<string:race_name>', endpoint='race_posts')
def posts_by_race(race_name):
    race_name = race_name # /terran, /protoss, /zerg
    posts = Post.query.filter_by(races=race_name).all()
    title = Post.query.filter_by(races=race_name).first()

    if not posts:
        return render_template('404.html')

    if race_name in ['zerg', 'terran', 'protoss']:

        return render_template('builds.html', posts=posts, race_name=race_name, title=title)
    else:
        return redirect(url_for('main.error'))

@posts.route('/<string:race_name>/<int:post_id>', endpoint='post')
def post(race_name, post_id):
    race_name = race_name
    post = Post.query.filter_by(races=race_name, id=post_id).first()

    if not post:
        return redirect(url_for('main.error'))
    else:
        return render_template('build.html', post=post, race_name=race_name)

@posts.route("/<string:race_name>/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(race_name, post_id):
    race_name = race_name.lower()
    post = Post.query.get_or_404(post_id)

    validate = Post.query.filter_by(races=race_name, id=post_id).first()

    if post.author != current_user:
        abort(403)

    if not validate:
        return redirect(url_for('main.error'))
    form = PostForm(obj=post)

    if form.validate_on_submit():

        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.races = form.races.data[0].lower()
        post.levels = form.levels.data[0].lower()
        post.content = form.content.data

        db.session.commit()
        race_name=post.races

        flash("Post has been updated!", "success")
        return redirect(url_for('posts.post', post_id=post.id, race_name=race_name))
    elif request.method == 'GET':

        level = []
        level.postsend(post.levels.capitalize())
        race = []
        race.postsend(post.races.capitalize())
        
        form.title.data = post.title
        form.subtitle.data = post.subtitle
        form.races.data =  race
        form.levels.data = level
        form.content.data = post.content


    else:
        print("Form Errors:", form.errors)  # Print out form validation errors
        print("Form Data:", form.data)    # Print out form data to inspect

    return render_template('create.html', legend="Update Post", form=form, race_name=race_name, post=post)

@posts.route("/<string:race_name>/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(race_name, post_id):
    race_name = race_name.lower()
    post = Post.query.get_or_404(post_id)

    validate = Post.query.filter_by(races=race_name, id=post_id).first()

    if not validate:
        return redirect(url_for('main.error'))
    
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted!", "success")
    return redirect(url_for('main.index'))