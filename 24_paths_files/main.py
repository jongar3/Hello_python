#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent

with open(BASE_DIR / "Input" / "Names" / "invited_names.txt", mode= "r") as f:
    names = f.read().split("\n")
with open(BASE_DIR / "Input" / "Letters" / "starting_letter.txt", mode= "r") as f:
    letters = f.read().split("\n")

for name in names:
    with open(BASE_DIR / "Output" / "ReadyToSend" / f"letter_for_{name}.txt", mode= "w") as f:
        letters[0]= f"Dear {name}"
        to_write = "\n".join(letters)
        f.write(str(to_write))