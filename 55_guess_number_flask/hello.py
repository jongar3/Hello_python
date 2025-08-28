from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def inner():
        return "<b>" + function() + "</b>"
    return inner
def make_emphasis(function):
    def inner():
        return "<em>" + function() + "</em>"
    return inner
def make_underline(function):
    def inner():
        return "<u>" + function() + "</u>"
    return inner



@app.route("/")
@make_bold
@make_emphasis
@make_underline
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "<h1>Bye!</h1>"





if __name__=="__main__":
    app.run(debug=True)