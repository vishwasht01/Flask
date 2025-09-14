from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/marks'
app.secret_key = "key"
db = SQLAlchemy(app)


class Marks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.Integer, nullable=False)
    math = db.Column(db.Integer, nullable=False)
    science = db.Column(db.Integer, nullable=False)
    programming = db.Column(db.Integer, nullable=False)


@app.route('/')
def home():
    return render_template('example.html')


@app.route("/result/<int:score>")
def result(score):
    if "score" in session:
        print("This is a fresh session")
    if score >= 35:
        return redirect(url_for('passed', scores=score))
    else:
        return redirect(url_for('fail', sco=score))


@app.route('/passed/<int:scores>')
def passed(scores):
    return "You have passed the exam with a score of " + str(scores)


@app.route("/fail/<int:sco>")
def fail(sco):
    return "Sorry You have scored only " + str(sco) + " Chin Up Champ"


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == 'POST':
        st1 = int(request.form['lang'])
        nd2 = int(request.form['math'])
        rd3 = int(request.form['science'])
        th4 = int(request.form['program'])
        entry = Marks(lang=st1, math=nd2, science=rd3, programming=th4)
        db.session.add(entry)
        db.session.commit()
        total = (st1 + nd2 + rd3 + th4) / 4
        session["score"] = total
        return redirect(url_for('result', score=total))
    return render_template("submit.html")


@app.route('/logout')
def logout():
    session.pop("score", None)
    flash("Logged out old session", "info")
    return redirect(url_for('home'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
