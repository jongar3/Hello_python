import tkinter
from tkinter import IntVar

from vlc import libvlc_vlm_set_input

window = tkinter.Tk()
window.title("Hello tkinter")
window.minsize(800, 400)

##LABELS
my_label = tkinter.Label(text="I am a label", font=("Arial", 20, "bold"))
my_label.pack(side="left") ##Se also grid and place methods

my_label.config(bg="red", text="New text")

##BUTTONS
def button_clicked():
    print("I get clicked")
    my_label.config(text=f"{v_input.get()}", fg="green")

button = tkinter.Button(text="Click Me")
button.place(x=0, y=0)
button.config(command=button_clicked)

##ENTRYS
v_input=tkinter.Entry(width=30)
v_input.pack()

##MULTY LINE TEXTS
big_input=tkinter.Text(width=40, height=5)
big_input.insert(tkinter.END, "This is an example text of multy lines text input")
big_input.pack()
print(big_input.get("1.0","end"))

##SPIN BOX
def spin_action():
    print(spin_box.get())

spin_box=tkinter.Spinbox(width=5, from_=1, to=10, command= spin_action)
spin_box.pack()
##SCALE BOX
def scale_action(value):
    print(scale_box.get())
    print(value)

scale_box=tkinter.Scale(from_=0, to=100, command= scale_action)
scale_box.pack()


##CHECK BUTTON
def check_action():
    print(state.get())

state= tkinter.IntVar()
check_button=tkinter.Checkbutton(window, text="Is it on?", command=check_action, variable=state)
check_button.pack()
##RADIO BUTTON
def radio_action():
    print(radio_state.get())

radio_state=tkinter.IntVar()
radio_button1=tkinter.Radiobutton(text="option 1", variable=radio_state, value=1, command= radio_action)
radio_button2=tkinter.Radiobutton(text="option 2", variable=radio_state, value=2, command= radio_action)
radio_button1.pack()
radio_button2.pack()
##LIST BOX
def listbox_action(event):
    print(listbox.get(listbox.curselection()))
    print(event)
listbox=tkinter.Listbox(width=30, height=4)
fruits= ["apple", "banana", "cherry", "orange"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_action)
listbox.pack()


window.mainloop()