from flask import Flask


app = Flask(__name__)


@app.route("/wd")
def index():
    return "Hello Flask!"


print("app.py")
print(__name__)


if __name__ == "__main__":
    app.run()
