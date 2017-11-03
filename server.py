from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "ThisisSecret"



@app.before_first_request
def before_load():
	session['counter'] = 0

@app.route('/')
def index ():
	session['counter'] += 1
	return render_template ('index.html')

@app.route('/add', methods=['POST'])
def double():
	session['counter'] += 1
	return redirect ('/')

@app.route('/clear', methods=['POST'])
def reset():
	session['counter'] = 0
	return redirect ('/')

app.run(debug=True)