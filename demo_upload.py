"""
  Created by Even on 2019-6-15
"""
from flask import Flask, render_template, request, redirect, url_for, make_response
from werkzeug.routing import BaseConverter

app = Flask(__name__)


@app.route("/upload", methods=["GET"])
def upload():
    return render_template("upload.html")


@app.route("/deal_upload", methods=["POST"])
def deal_upload():
    file = request.files.get("demo")
    file.save("./demo.png")
    return "Success"