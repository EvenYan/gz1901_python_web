"""
  Created by Even on 2019-6-15
"""
from flask import Flask, g, abort

app = Flask(__name__)


count = 8

@app.route("/")
def index():
    print("你获得了%s折的优惠券")
    return "你获得了%s折的优惠券"%count


@app.before_first_request
def handle_before_first_request():
    global count
    print("in handle_before_first_request")
    count = 1


@app.before_request
def handle_first_request():

    print("in handle_first_request")


@app.after_request
def handle_after_requst(respose):
    print("in handle_after_requst func")
    return respose


@app.teardown_request
def handle_teardown_request(response):
    global count
    print("in handle_teardown_request func")
    count = 8
    return response
