import flask
from flask import request

app=flask.Flask(__name__)


@app.route("/")
def get_index():
    return flask.render_template("index.html")


@app.post("/login")
def get_login():
    if request.method=="POST":
        print(request.form)
        email=request.form.get("email")
        password=request.form.get("password")
        return flask.render_template("login.html", email=email, password=password)
    else:
        return "Something went wrong"


if __name__=="__main__":
    app.run(debug=True)