BASE_EMAIL = "example@gmail.com"
# ---------------------------- READ DATA FILE ------------------------------- #
import pathlib
import json
PATH = pathlib.Path(__file__).parent 
data_dict={}  # Initialize an empty dictionary to store data

data_path = PATH / "data.txt"

try:
    json_file = open(PATH / "data.json")

except FileNotFoundError:
    if data_path.exists():
        with open(data_path, "r") as file:
            data = file.read().split("\n")
            for line in data:
                line_list=line.split(" | ")
                if len(line_list)!=3:
                    continue
                website = line_list[0]
                email = line_list[1]
                password = line_list[2]
                if website not in data_dict:
                    data_dict[website] = {"email": [], "password": []}
                data_dict[website]["email"].append(email)
                data_dict[website]["password"].append(password)
        print(data_dict) 

else: 
    data_dict = json.load(json_file)
    json_file.close()
    #print(data_dict)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import messagebox 
def generate_password():
    import random
    import string
    email = email_entry.get()
    website = website_entry.get()
    if not (email and website):
        messagebox.showwarning(title="Insuficient data", message="Please fill the website and email fields.")
        return
    # Generate a random password
    length = random.randint(10, 16)  # Random length between 12 and 16
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    messagebox.showinfo(title="Generated Password", message=f"Password generated: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_data():
    with open(data_path, "w") as file:
        for website in data_dict:
            for index, email in enumerate(data_dict[website]["email"]):
                file.write(f"{website} | {email} | {data_dict[website]['password'][index]}\n")
    # Save the data to a JSON file
    with open(PATH / "data.json", "w") as json_file:
        json.dump(data_dict, json_file, indent=4)

def save_password():
    global data_dict
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
   
    if not (website and email and password):
        messagebox.showwarning(title="Insuficient data", message="Please fill all fields.")
        return
    elif website in data_dict and email in data_dict[website]["email"]:
        messagebox.showwarning(title="Duplicate Entry", message=f"An entry for {website} with this email already exists.")
        return
    if messagebox.askokcancel(title="Confirm Save", message=f"Do you want to save the password for {website}?\nEmail: {email}\nPassword: {password}"):
        if website not in data_dict:
            data_dict[website] = {"email": [], "password": []}
        data_dict[website]["email"].append(email)
        data_dict[website]["password"].append(password)
        write_data()
        window.clipboard_clear()
        window.clipboard_append(password)
        window.update()
        messagebox.showinfo(title="Success", message=f"Password for {website} saved and copied to the clipboard!")
        
    # Write the updated data back to the file
    # with open(data_path, "w") as file:
    #     for site, info in data_dict.items():
    #         for i in range(len(info["email"])):
    #             file.write(f"{site} | {info['email'][i]} | {info['password'][i]}\n")
    
    # Clear the entries after saving
    website_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    email_entry.insert(0, BASE_EMAIL)  # Reset email entry to default
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website=website_entry.get().strip()
    email=email_entry.get().strip()
    if website:
        try: 
            passwords = data_dict[website]["password"]
            emails = data_dict[website]["email"]
        except KeyError:
            messagebox.showarning(title="No data", message=f"No data found for {website}.")
            return
        else: 
            message = "\n".join(f"Email: {e}, Password: {p}" for e, p in zip(emails, passwords))
            messagebox.showinfo(title=f"Password for {website}", message=message)
            del message
    else:
        messagebox.showwarning(title="Insuficient data", message="Please fill the website and email fields.")
        return
# ---------------------------- UI SETUP ------------------------------- #

import tkinter as tk

window = tk.Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, bg="white")
canvas= tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
image_tk = tk.PhotoImage(file= str(PATH / "logo.png"))  # Load the logo image
canvas.create_image(100, 100, image=image_tk)  
canvas.grid(row=0, column=1, padx=10, pady=10)

##Create Labels
website_label = tk.Label(text="Website:", bg="white")
email_label = tk.Label(text="Email/Username:", bg="white")
password_label = tk.Label(text="Password:", bg="white")
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

##Create Entries
website_entry = tk.Entry(width=20)
email_entry = tk.Entry(width=35)
password_entry = tk.Entry(width=20)
email_entry.insert(0, BASE_EMAIL)  # Set the default email
email_entry.grid(row=2, column=1, columnspan= 2)
website_entry.grid(row=1, column=1)
password_entry.grid(row=3, column=1)
##Create buttons
generate_button = tk.Button(text="Generate Password", command=generate_password, width= 15, font=("Arial", 8))
add_button = tk.Button(text="Add", width=40, font=("Arial", 8), command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
search_button = tk.Button(text="Search", width=15, font=("Arial", 8), command=search_password)
generate_button.grid(row=3, column=2)
search_button.grid(row=1, column=2)
window.mainloop()