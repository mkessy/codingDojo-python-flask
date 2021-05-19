from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_user import User
from flask_app.models.model_movie import Movie
from flask_app.models.model_review import Review

@app.route('/')
def index():
    if 'uuid' not in session:
        return redirect('/login')
    return redirect('/dashboard')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/login')

    # movie_names = []
    # movies = Movie.get_all()
    # for movie in movies:
    #     movie_names.append(movie.display_title())
    
    context = {
        "logged_in_user": User.get_one(session['uuid']),
        # "movie_titles": movie_names
        "all_movies": Movie.get_all()
    }
    return render_template('dashboard.html', **context)