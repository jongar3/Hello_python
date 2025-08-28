import pathlib
from flask import Flask
from random import randint
app = Flask(__name__)

CURRENT_DIR= pathlib.Path(__file__).parent.resolve()

def read_file(file_name):
    with open(CURRENT_DIR / file_name, "r") as file:
        code= file.read()
    return code

number= randint(0,9)

@app.route("/")
def def_index():
    return read_file("index.html")

@app.route("/<int:user_number>")
def show_high_low(user_number):

    if user_number> number:
        return read_file("to_high.html")
    elif user_number< number:
        return read_file("to_low.html")
    else:
        return read_file("you_guessed.html")






if __name__== "__main__":
    app.run(debug=True)
