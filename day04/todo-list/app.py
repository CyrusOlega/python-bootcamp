from flask import Flask, url_for, redirect, abort, request, render_template, session

app = Flask(__name__)
app.secret_key = 'secret_key'

todo_list = [
        {"title": "Task 1", "description": "Do this task", "is_complete": False},
        {"title": "Task 1", "description": "Do this task", "is_complete": False},
        {"title": "Task 1", "description": "Do this task", "is_complete": False}
    ]

@app.get("/")
def home():
    if session.get("todo_list"):
        todo_list = session.get("todo_list")
    else:
        todo_list = []

    return render_template("index.html", items=todo_list)

@app.post("/")
def home_post():
    return redirect("/")

app.run()