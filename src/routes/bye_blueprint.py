from flask import Blueprint, redirect, url_for

bye_blueprint = Blueprint("bye_blueprint", __name__, template_folder="../../templates")

@bye_blueprint.route("/")
def index():
    return "Bye world"

@bye_blueprint.route("/<name>")
def bye(name):
    return f"Bye {name}"

@bye_blueprint.route("/hello/<name>")
def redirect_bye(name):
    return redirect(url_for("hello_blueprint.html_greeting", name=name))