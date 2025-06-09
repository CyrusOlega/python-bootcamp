from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/profile/")
@app.route("/profiles/")
def profile():
    return "Profile Page"

@app.route("/profile/<username>")
def dynamic_profile(username):
    return f"Profile {username} Page"

app.run()