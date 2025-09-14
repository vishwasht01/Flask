from doctest import debug

from flask import Flask,redirect,url_for
app = Flask(__name__)
@app.route('/home')
def home():
    return "Hello this is main page"

@app.route('/<name>')
def username(name):
    return f" Hello : {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)