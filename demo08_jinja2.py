"""
  Created by Even on 2019-6-15
"""
from flask import Flask, g, abort, render_template

app = Flask(__name__)


count = 8

@app.route("/<username>")
def index(username):
    peoples = ["Alice", "Tom"]
    return render_template("index.html", peoples=peoples)
