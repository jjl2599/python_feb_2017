from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'thisissecret'
import random


@app.route('/')
def start():
    if 'totalgold' not in session:
        session['totalgold'] = 0
    if 'result' not in session:
        session['result'] = []
    return render_template("main.html")

@app.route('/process_money', methods=['POST'])
def display():
    if request.form['building'] == 'farm':
        num = random.randint(10,20)
        session['totalgold'] += num
    elif request.form['building'] == 'cave':
        num = random.randint(5,10)
        session['totalgold'] += num
    elif request.form['building'] == 'house':
        num = random.randint(2,5)
        session['totalgold'] += num
    elif request.form['building'] == 'casino':
        chance = random.randint(1,2)
        if chance == 1:
            num = random.randint(0,50)
            session['totalgold'] += num
        elif chance == 2:
            num = random.randint(-50,0)
            session['totalgold'] += num
            
    if num >= 0:
        event = "Earned"
    elif num < 0:
        event = "Lost"

    str= "{} {} gold from the {}".format(event,abs(num),request.form['building'])
    session['result'].insert(0,str)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
