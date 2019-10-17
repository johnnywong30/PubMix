#########################
#
#   Johnny Wong
#   Flask App for PubMix
#
#########################
import os

from flask import Flask, render_template, redirect, url_for, session, request, flash, get_flashed_messages
from util import db

# instantiate Flask Object
app = Flask(__name__)
app.secret_key = os.urandom(32)

DB_FILE = "data/pubmix.db"
db.create_db()

@app.route("/")
def login():
    '''Login Page'''
    return render_template('index.html')

@app.route("/register")
def register():
    '''Register Page'''
    return render_template('register.html')

@app.route("/authenticate", methods=['POST'])
def authenticate():
    '''Authenticates user on login/register attempt'''
    # Login
    if request.form['submit'] == "Login":
        username, password = request.form['username'], request.form['password']
        if len(username.strip()) != 0 and len(password.strip()) != 0 and db.verify_user(username, password):
            session['username'] = username
            url = "home"
        elif db.find_user(username):
            flash("Incorrect password!")
            url = "login"
        else:
            flash("Incorrect credentials!")
            url = "login"
    # Register
    if request.form['submit'] == "Register":
        username, password, confirm = request.form['username'], request.form['password'], request.form['confirm']
        if password != confirm:
            flash("Passwords don't match!")
            url = "register"
        elif ' ' in username or len(username.strip()) == 0:
            flash("Invalid username!")
            url = "register"
        elif db.find_user(username):
            flash("Username exists!")
            url = "register"
        elif ' ' in password or len(password.strip()) == 0:
            flash("Invalid password!")
            url = "register"
        else:
            db.register_user(username, password)
            flash("Successfully registered user '{0}'".format(username))
            url = "login"
    return redirect(url_for(url))

@app.route("/logout")
def logout():
    '''Logs user out'''
    if 'username' not in session:
        return redirect(url_for("login"))
    session.pop('username', None)
    flash("Successfully logged out!")
    return redirect(url_for("login"))



@app.route("/home")
def home():
    '''Home Page'''
    if 'username' not in session:
        return redirect(url_for("login"))
    return render_template("home.html")




if __name__ == "__main__":
    app.debug = True
    app.run()
