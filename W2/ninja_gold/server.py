from flask import Flask, render_template, redirect, request,session
app = Flask(__name__)
app.secret_key= 'hey'
import random
@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
    return render_template('index.html')

@app.route('/reset')
def clear():
    session.clear()
    return redirect('/')

locations = {'farm':(10,20),'cave':(5,10),'house':(2,5),'casino':(-50,50)}

@app.route('/process_money', methods=['POST'])
def process_money():
    color = 'green'
    msg = "earned"
    if request.form['location'] == 'farm':
        gold = random.randint(10,20)
    elif request.form['location'] == 'cave':
        gold = random.randint(5,10)
    elif request.form['location'] == 'house':
        gold = random.randint(2,5)
    elif request.form['location'] == 'casino':
        gold = random.randint(-50,50)
        if gold < 0:
            color = 'red'
            msg = 'lost'
    session['activities'].append(f"player <span class='{color}'> {msg} </span> {gold} from {request.form['location']}!")
    session['gold'] += gold
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True) 