import flask 
import smtplib
from email.message import EmailMessage
from flask import render_template, request
import pathlib, json
import dotenv, os

dotenv.load_dotenv()

CURRENT_DIR= pathlib.Path(__file__).parent.resolve()
PASSWORD= os.getenv("PASSWORD")
MY_EMAIL= os.getenv("MY_EMAIL")


def get_data(file_path):
    with open(file_path, 'r') as r:
        data= json.load(r)
    return data


def send_email(name, email, msg, phone):
    msg = EmailMessage()
    msg["Subject"] = f"{name} is trying to contact"
    msg["From"] = MY_EMAIL
    msg["To"] = MY_EMAIL
    msg.set_content(f"Name {name}.\nPhone {phone}.\nEmail {email}.\n msg {msg}")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(MY_EMAIL, PASSWORD)
        connection.send_message(msg)





app = flask.Flask(__name__)



@app.route("/index.html")
@app.route("/")
def home():
    data= get_data(CURRENT_DIR / "static/blog-data.txt")
    return render_template("index.html", data=data)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.post("/contact.html")
@app.route("/contact")
@app.route("/contact.html")
def contact():
    name=request.form.get("name")
    email=request.form.get("email")
    phone=request.form.get("phone_number")
    msg=request.form.get("message")
    if email:
        send_email(email=email, name=name, phone=phone, msg=msg)
    return render_template("contact.html", email=email)
@app.post("/receive_data")
def receive_data():
    print(request.form)
    return "data received!"

@app.route("/post.html/<num>")
def post(num):
    num=int(num)
    data= get_data(CURRENT_DIR / "static/blog-data.txt")
    content= data[num-1]
    return render_template("post.html", content=content)



if __name__ == "__main__":
    app.run(debug=True)
