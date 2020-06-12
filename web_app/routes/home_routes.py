# web_app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return "Welcome to Katie's Twitoff Assignment."

@home_routes.route("/about")
def about():
    return "About me"