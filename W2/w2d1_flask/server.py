from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "inconceivable!"

# Display
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html")

# Action 
@app.route('/process', methods=['POST'])          # The "@" decorator associates this route with the function immediately following
def process():
    # name = request.form['name']
    session['uuid'] = request.form['name']
    # return render_template('processData.html', name=name)
    return redirect('/success')

# Display 
@app.route('/success')          # The "@" decorator associates this route with the function immediately following
def success():
    if not "uuid" in session:
        return redirect('/')
    
    uuid = session['uuid']
    return render_template('processData.html', uuid=uuid)







if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode