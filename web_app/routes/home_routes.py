from flask import Flask
from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    #x = 2 + 2
    return f"Welcome to Katie's twitoff assignment"

@home_routes.route("/about")
def about():
    return "About me"