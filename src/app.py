from flask import Flask, render_template
from flask_cors import CORS


app = Flask(
    __name__, static_folder="../static", template_folder="../templates"
)
CORS(app)


@app.get("/")
def everything_is_okay():
    return render_template("index.html")
