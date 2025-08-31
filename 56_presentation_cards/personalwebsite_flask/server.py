from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/Pages/Contact.html")
def Contact(): 
    return render_template("Contact.html")
@app.route("/Pages/Hobbies.html")
def Hobbies():
    return render_template("Hobbies.html")

if __name__=="__main__":
    app.run(debug=True)