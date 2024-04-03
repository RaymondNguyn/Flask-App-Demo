from flask import Flask, render_template, jsonify, request, abort

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)