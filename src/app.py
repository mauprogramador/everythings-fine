from flask import Flask, redirect, render_template
from flask_cors import CORS
from werkzeug.exceptions import HTTPException


app = Flask(
    __name__, static_folder="../static", template_folder="../templates"
)
CORS(app)


@app.get("/")
def everything_is_fine():
    return render_template("index.html")


@app.errorhandler(HTTPException)
def handle_http_exceptions(_):
    return redirect("/")


@app.errorhandler(400)
def handle_bad_request(_):
    return redirect("/")


@app.errorhandler(404)
def handle_not_found(_):
    return redirect("/")
