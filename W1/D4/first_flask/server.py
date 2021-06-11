from flask import Flask, render_template, redirect, session, request  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
import random

app.secret_key = """7ded47dda35069e3e424062e85684f8e
d43737818ed8f1da279f3c225d54f4c5
079ac83b2b3b0ecc75620d751fd0a9a0
4d8aa78765fa5703fb12ec1d32609884
0b8e536077e47ae458edb551eb866669
369cf345d1bcc559888daa334c961a40
036cbd0ed065b006d5ca234a684af288
7c2d5923f49e7d6d309d08ef463a609d
21c2f36fdbedd03cdaabc117a9c540fb
7c75e8d1ff12091cf07761cb19104fad"""

# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response

# Display route
@app.route('/dashboard')
@app.route('/new_page')
@app.route('/dashboard/<color>')
def dashboard(color="white"):
    session['uuid'] = 1
    return render_template('dashboard.html', color=color)

# Action route
@app.route('/dashboard/<int:num>/<name>/<int:age>')
def print_num(num, name, age):
    print(num)
    session['number'] = num
    session['name'] = name
    session['age'] = age
    return redirect('/new_page')

# Action route
@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/dashboard')

# Action route
@app.route('/display_data', methods=['POST'])
def display_data():
    print(request.form)
    session['ssn'] = request.form['ssn']
    return redirect('/dashboard')



# *****************************************************

@app.route('/')
def ninja_game():
    if 'user_gold' not in session:
        session['user_gold'] = 0
        session['activity'] = []
    return render_template('ninja_gold.html')

@app.route("/reset")
def reset():
    session.clear()
    return redirect('/')

@app.route('/process_money', methods=['POST'])
def process_money():

  #location_dict = {"cave": "", "house": "", "farm": "", "casino": ""}
    if request.form["location"] == "house":
        gold_to_add= random.randint(2,5)

    elif request.form["location"] == "cave":
        gold_to_add = random.randint(5,10)   

    elif request.form["location"] == "farm":
        gold_to_add = random.randint(10,20)

    elif request.form["location"] == "casino":
        gold_to_add = random.randint(-50,50)
        
    session['user_gold'] += gold_to_add
    if gold_to_add < 0:
        session['activity'].append(f"<h2 style='color:red'> You walked in the casino and lost {(gold_to_add)*-1}... owch! </h2>")

    else:
        session['activity'].append(f"<h2 style='color:green'> Earned {gold_to_add} golds from the {request.form['location']}! </h2>")

    return redirect('/')






if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode