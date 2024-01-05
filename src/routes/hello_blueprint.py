from flask import Blueprint, render_template

hello_blueprint = Blueprint("hello_blueprint", __name__, template_folder="../../templates")

@hello_blueprint.route("/")
def index():
    return "Hello world"

@hello_blueprint.route("/hello/<name>")
def greeting(name):
    return f"Hello {name}"

@hello_blueprint.route("/hellohtml/<name>")
def html_greeting(name):
    return render_template("hello.html", name=name)