import json

from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/wd")
def index():
    return "Hello word!"


@app.route("/")
def home():
    people_info = {"name": "Tom", "age": 20, "sex": "male"}

    return jsonify(people_info)



if __name__ == "__main__":
    app.run(debug=True)
