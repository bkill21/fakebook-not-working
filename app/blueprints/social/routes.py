from flask import render_template
from . import bp
from flask_login import current_user

from app.models import Post
from app.forms import PostForm


@bp.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        p.user_id = current_user.user_id
        p = Post(body=form.body.data)
        p.commit()
        print(f'{p.author = } {p.author.posts[0]}')
    return render_template('post.jinja', form=form)

