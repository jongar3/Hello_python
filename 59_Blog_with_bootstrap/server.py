import flask 
from flask import render_template
import pathlib, json
CURRENT_DIR= pathlib.Path(__file__).parent.resolve()

def get_data(file_path):
    with open(file_path, 'r') as r:
        data= json.load(r)
    return data


app = flask.Flask(__name__)



@app.route("/index.html")
@app.route("/")
def home():
    data= get_data(CURRENT_DIR / "static/blog-data.txt")
    return render_template("index.html", data=data)

@app.route("/about.html")
def about():
    return render_template("about.html")
@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/post.html/<num>")
def post(num):
    num=int(num)
    data= get_data(CURRENT_DIR / "static/blog-data.txt")
    content= data[num-1]
    return render_template("post.html", content=content)



if __name__ == "__main__":
    app.run(debug=True)
