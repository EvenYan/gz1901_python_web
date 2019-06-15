"""
  Created by Even on 2019-6-15
"""
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.routing import BaseConverter

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


@app.route("/subpath/<path:subpath>")
def get_post(subpath):
    return subpath


class PhoneConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super().__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        return "xxx"

    def to_url(self, value):
        value = str(value)
        return value[:1] + "****" + value[10:]



app.url_map.converters['re'] = PhoneConverter


@app.route("/check_number/<re(r'1.{4}\d'):phone_number>")
def check_number(phone_number):
    return phone_number


@app.route("/dail/<int:phone_number1>")
def dail_number(phone_number1):
    url = url_for("check_number", phone_number=phone_number1)
    return redirect(url)