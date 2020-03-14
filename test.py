from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Deployed</h1>'