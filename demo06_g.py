"""
  Created by Even on 2019-6-15
"""
from flask import Flask, g


app = Flask(__name__)


@app.route("/")
def index():
    return str(g.b)


@app.route("/<int:a>/<int:b>")
def func(a, b):
    g.a = a
    g.b = b
    ret = sum1()
    print(ret)
    return str(ret)


def sum1():
    ret = sum2()
    return ret


def sum2():
    total = g.a + g.b
    return total