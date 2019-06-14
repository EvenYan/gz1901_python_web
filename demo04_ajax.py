import json

from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/wd")
def index():
    return "Hello word!"


@app.route("/")
def home():

    return render_template("ajax.html")


@app.route("/get_info")
def get_info():

    import time
    time.sleep(5)
    return jsonify({"name": "Tom", 'age': 30})


if __name__ == "__main__":
    app.run(debug=True)
