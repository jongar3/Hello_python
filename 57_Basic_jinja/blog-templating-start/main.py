from flask import Flask, render_template
import requests


app = Flask(__name__)

data= requests.get("https://api.npoint.io/f8f8edf48cf18b78ab97")
data=data.json()
for index,dat in enumerate(data["list"]):
    dat["id"]= index #Objeto mutable

print(data)

@app.route('/')
def home():
    return render_template("index.html", data=data["list"])

@app.route("/post/<int:index>")
def get_post(index):
    print(data["list"][index]["text"])
    return render_template("post.html", text= data["list"][index])





if __name__ == "__main__":
    app.run(debug=True)
