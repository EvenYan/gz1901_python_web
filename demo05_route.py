"""
  Created by Even on 2019-6-15
"""
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/index")
@app.route("/", methods=["GET"])
def index():
    return render_template("login.html")


@app.route("/", methods=["POST"])
def index1():
    return "index1"


@app.route("/login", methods=["GET", "POST"])
def login():
    name = request.form.get("username")
    passwd = request.form.get("passwd")
    print(name)
    print(passwd)
    return name + ":" + passwd


@app.route("/new_url")
def new_func():
    return "new_url"


@app.route("/old_url")
def old_func():
    new_url = url_for("new_func")
    return redirect(new_url)
