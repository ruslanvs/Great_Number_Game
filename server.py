import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "MyEducationalSession"

@app.route( "/" )
def front_page():
    if "random_number" not in session:
        session["random_number"] = random.randrange( 0, 101 )
    print "The random number in this session is:", session["random_number"]
    return render_template( "index.html" )

@app.route( "/result", methods = ["POST"] )
def result():
    last_user_form_input_guess_nr_captured_in_python = "You guessed - " + request.form["user_form_input_guess_nr"]
    if int(request.form["user_form_input_guess_nr"]) > session["random_number"]:
        result = "Too high!"
    elif int(request.form["user_form_input_guess_nr"]) < session["random_number"]:
        result = "Too low!"
    else:
        result = "CORRECT!"

    return render_template( "index.html", result = result, last_user_form_input_guess_nr_for_page = last_user_form_input_guess_nr_captured_in_python )

@app.route( "/reset", methods = ["POST"] )
def reset():
    session.clear()
    return redirect( "/" )

app.run( debug = True )