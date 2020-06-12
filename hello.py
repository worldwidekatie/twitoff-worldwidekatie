# hello.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    x = 2+2
    return f"Hello World! {x}"

@app.route("/about")
def about():
    print("VISITING THE ABOUT PAGE")
    return "About me"

# FLASK_APP=hello.py flask run