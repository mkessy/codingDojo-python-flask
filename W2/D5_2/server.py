from flask_app import app

from flask_app.controllers import controller_dogs, controller_collar, controller_routes, controller_toys

if __name__=="__main__":
    app.run(debug=True)