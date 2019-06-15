"""
  Created by Even on 2019-6-15
"""
from flask import Flask, render_template, request, redirect, url_for, make_response
from werkzeug.routing import BaseConverter

app = Flask(__name__)


@app.route("/", methods=['POST', "GET"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        passwd = request.form.get("passwd")
        response = make_response(render_template("userinfo.html", username=username))
        response.set_cookie("name", username)
        return response
    return render_template("login.html")


@app.route("/logout")
def logout():
    response = make_response("退出成功")
    response.delete_cookie("name")
    return response