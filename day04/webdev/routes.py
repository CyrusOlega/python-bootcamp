from flask import Flask, url_for, redirect, abort, request, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
@app.route("/index/")
def home():
    return f"""
    <h1>Welcome to my page</h1>
    <p>This is where everything begins!</p>
    
    <h2>Table of Contents</h2>
    <ul>
        <li><a href="{url_for('dynamic_topic', topic="About Me")}">About Me</li>
        <li><a href="{url_for('dynamic_topic', topic="My Posts")}">My Posts</li>
        <li><a href="{url_for('dynamic_topic', topic="Contacts")}">My Contact Details</li>
    </ul>
    <a href="{url_for('login_get')}">Login Page</a>
    <a href="{url_for('profile', username="Ace")}">Ace</a>
    """

@app.route("/home/<name>")
@app.route("/index/<name>")
def dynamic_home(name):
    return f"""
    <h1>Welcome to my page {name}</h1>
    <p>This is where everything begins!</p>
    
    <h2>Table of Contents</h2>
    <ul>
        <li><a href="/page/About Me">About Me</li>
        <li><a href="/page/My Posts">My Posts</li>
        <li><a href="/page/Contacts">My Contact Details</li>
    </ul>
    <a href="{url_for('login_get')}">Login Page</a>
    <a href="{url_for('profile', username="Ace")}">Ace</a>
    """

def valid(username, email, password):
    return (
        username == "admin"
        and password == "pass"
        and email == "admin@gmail.com"
    )

@app.post("/login")
def login_post():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    print(username)
    print(email)
    print(password)

    if not valid(username, email, password):
        return "Invalid credentials"
    else:
        return "Login Successful"

@app.route("/page/<topic>")
def dynamic_topic(topic):
    return f"""
    <h1>Viewing page for {topic}</h1>
    <a href="/">Return to Home</a>
"""

@app.get('/login')
def login_get():
    return render_template("index.html")

@app.route("/profile/<username>")
def dynamic_profile(username):
    return render_template(
        "profile.html",
        username=username
    )

@app.route("/profile/<username>")
def profile(username):
    if username != "admin":
        return redirect(url_for('login_get'))
    else:
        return "Welcome Admin"

@app.errorhandler(501)
def not_implemented(error):
    return "Not implemented yet"

app.run()