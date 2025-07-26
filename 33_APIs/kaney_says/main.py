from tkinter import *
import requests
import pathlib
BASE_PATH = pathlib.Path(__file__).parent
def get_quote():
    URL= "https://api.kanye.rest"
    #Write your code here.
    response = requests.get(URL)
    response.raise_for_status()  # Check for request errors
    data_json = response.json()
    quote = data_json["quote"]
    canvas.itemconfig(quote_text, text=quote, font= ("Arial", 17, "bold"), fill="white")

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=BASE_PATH / "background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=BASE_PATH / "kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()