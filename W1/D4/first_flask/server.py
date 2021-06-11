from flask import Flask, render_template, redirect  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# Display route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Action route
@app.route('/dashboard/<int:num>/<name>/<int:age>')
def print_num(num, name, age):
    print(num)
    context = {
        "age": age,
        "number": num,
        "name": name,
    }
    return render_template('the_num_page.html', **context)













if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode