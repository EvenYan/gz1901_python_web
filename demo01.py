from flask import Flask, render_template

app = Flask(__name__)


@app.route("/wd")
def index():
    return "Hello word!"


@app.route("/")
def home():
    people_list = ["Tom", "Merry", "Jim"]
    return render_template("index.html", peoples=people_list)


@app.route("/user_info/<username>")
def user_info(username):
    return render_template("user_info.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)
