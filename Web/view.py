from flask_web import app
from flask import render_template

#rotas
@app.route("/")
def homepage():
    return render_template("Home.html")

@app.route("/teste")
def teste():
    return "voce me achou"

@app.route("/profile")
def profile():
    return render_template("Profile.html")
