from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_post import Post

@app.route('/post/new')
def post_new():
    return render_template('post_new.html')

@app.route('/post/create', methods=['POST'])
def post_create():
    info = {
        **request.form,
        'user_id': session['uuid'] 
    }
    Post.create(info)
    return redirect('/')

@app.route('/post/<int:post_id>/delete')
def post_delete(post_id):
    post = Post.get_one(post_id)

    print(f"post user_id: {post['user_id']} || uuid: {session['uuid']}")

    if post['user_id'] == session['uuid']:
        Post.delete_one(post_id)
    return redirect('/')

@app.route('/post/<int:post_id>/edit')
def post_edit(post_id):
    context = {
        "post" : Post.get_one(post_id)
    }
    return render_template('post_edit.html', **context)

@app.route('/post/<int:post_id>/update', methods=['POST'])
def post_update(post_id):
    info = {
        **request.form,
        "id": post_id
    }
    Post.update_one(info)
    return redirect('/')