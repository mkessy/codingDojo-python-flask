from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_movie import Movie

@app.route('/movie/new')
def new_movie():
    return render_template('movie_new.html')

@app.route('/movie/create', methods=['POST'])
def create_movie():
    # validate movies
    is_valid = Movie.validate_movie(request.form)

    if is_valid:
        # edge case = check to see if movie already exists
        # create move
        new_movie_id = Movie.new(request.form)
        return redirect(f'/movie/{new_movie_id}/view')
    return redirect('/movie/new')

# This is a DISPLAY route
@app.route('/movie/<int:movie_id>/edit')
def edit_movie(movie_id):
    # get the movie
    context = {
        "movie" : Movie.get_one(movie_id)
    }
    print(context)
    # render the template
    return render_template('movie_edit.html', **context)

# This is a ACTION route
@app.route('/movie/<int:movie_id>/update',  methods=['POST'])
def update_movie(movie_id):
    # process movie info
    Movie.update_one(id, request.form)
    # return to dashboard   
    return redirect(f'/movie/{movie_id}/view')

@app.route('/movie/<int:movie_id>/view')
def view_movie(movie_id):
    # get movie
    context = {
        "movie": Movie.get_one(movie_id)
    }
    # render
    return render_template('movie_view.html', **context)

@app.route('/movie/<int:movie_id>/delete')
def delete_movie(movie_id):
    Movie.delete_one(movie_id)
    return redirect('/')

