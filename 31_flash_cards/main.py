import tkinter as tk
import pathlib
import random
##Constants
BASE_PATH = pathlib.Path(__file__).parent
PHOTO_DIR= BASE_PATH / "images"
DATA_DIR = BASE_PATH / "data"
BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- DATA SETUP ------------------------------- #
import pandas as pd
try: 
    data= pd.read_csv(DATA_DIR / "french_words.csv")
except FileNotFoundError:
    print("File not found. Please ensure the 'french_words.csv' file is in the 'data' directory.")
    raise FileNotFoundError ("French words data file is missing.")

print(data)
total_words = len(data)
french_word2learn= list(data.French)
current_french_word = None
after_id = None  # Variable to store the ID of the after method for flipping the card
#-----------------------------DEFINE MAIN FUNCTIONS------------------------------- #
def know_the_word():
    """Removes the current word from the list then updates the card to the next word."""
    if current_french_word is not None:
        french_word2learn.remove(current_french_word)
    print(len(french_word2learn))
    next_card()  # Show the next card after removing the current one
def next_card():
    """Function to display the next card."""
    global current_french_word, after_id
    if after_id is not None:  # If a card is already flipped, cancel it
        window.after_cancel(after_id)
        after_id = None 
    current_french_word = random.choice(french_word2learn)
    canvas.itemconfig(canvas_image, image=front)
    canvas.itemconfig(canvas_language_text, text="French", font=("Ariel", 40, "italic"), fill="black")
    canvas.itemconfig(canvas_word_text, text=current_french_word, font=("Ariel", 60, "bold"), fill="black")
    after_id = window.after(3000, flip_card)  # Flip card after 3 seconds
def flip_card():
    """"Function to flip the card to show the other side."""
    global after_id
    after_id = None  # Reset after_id to prevent multiple flips
    canvas.itemconfig(canvas_image, image=back)
    canvas.itemconfig(canvas_language_text, text="English", font=("Ariel", 40, "italic"), fill="white")
    canvas.itemconfig(canvas_word_text, text=data[data.French==current_french_word].English.item(), font=("Ariel", 60, "bold"), fill="white")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flashi")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

#Buttons
right_image=tk.PhotoImage(file= str(PHOTO_DIR / "right.png"))
wrong_image=tk.PhotoImage(file= str(PHOTO_DIR / "wrong.png"))
button_right = tk.Button(image=right_image, highlightthickness=0, command=know_the_word)
button_wrong = tk.Button(image=wrong_image, highlightthickness=0, command=next_card)
button_right.grid(row=1, column=1)
button_wrong.grid(row=1, column=0)

#Canvas 
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front= tk.PhotoImage(file=str(PHOTO_DIR / "card_front.png"))
back= tk.PhotoImage(file=str(PHOTO_DIR / "card_back.png"))
canvas_image= canvas.create_image(400, 263, image=front)
canvas_language_text= canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas_word_text= canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

window.mainloop()

