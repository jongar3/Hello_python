import pathlib
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 #25
SHORT_BREAK_MIN = 5 #5
LONG_BREAK_MIN = 20 #20
CHECK_MARK= "✔"
PATH=pathlib.Path(__file__).parent # Get the path of the current file's directory

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    """Reset the timer to its initial state."""
    global n_times, count_down_after_id
    n_times = 0  # Reset the number of times the timer has been started
    l_checks.config(text="")
    display_time(0, 0)  # Reset the timer display to 00:00
    if count_down_after_id is not None:
        window.after_cancel(count_down_after_id)  # Cancel any ongoing countdown
        count_down_after_id = None  # Reset the countdown ID
    # Additional reset logic can be added here if needed
    l_timer.config(text= "Timer", font= (FONT_NAME, 28, "bold"), fg=GREEN, bg=YELLOW)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
count_down_after_id = None  # Initialize the countdown ID to None
n_times= 0  # Initialize the number of times the timer has been started
def start_timer():
    """Start the Pomodoro timer."""
    global n_times
    n_times = 0  # Reset the number of times the timer has been started
    set_timer()  # Call the set_timer function to initialize the timer

def set_timer():
    global count_down_after_id, n_times
    if count_down_after_id is not None:
        window.after_cancel(count_down_after_id) # Cancel any ongoing countdown
        count_down_after_id = None  # Reset the countdown ID    
    n_times += 1
    if n_times>=8:
        n_times = 0
        seg_time = LONG_BREAK_MIN * 60
        l_timer.config(text="Long break", fg=GREEN, font= (FONT_NAME, 28, "bold"))  # Change label text and color for long break
    elif n_times % 2 == 0:  # Even number means rest session
        seg_time=SHORT_BREAK_MIN * 60
        l_timer.config(text="Rest", fg=PINK, font= (FONT_NAME, 28, "bold"))
    else:  # Odd number means work session
        seg_time=WORK_MIN * 60
        l_timer.config(text="Work", fg=RED, font= (FONT_NAME, 28, "bold"))
        l_checks.config(text=CHECK_MARK * (n_times // 2 + 1))  # Update check marks based on completed work sessions
    display_time(seg_time // 60, seg_time % 60)  # Display the initial time in minutes and seconds
    count_down(seg_time)  # Start the countdown with the segment time
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(seg_time):
    global count_down_after_id
    seg_time -= 1  # Decrement the segment time by 1 second
   
    if seg_time<0: 
        window.deiconify()      # Show the window if it was hidden
        window.lift()           # Bring the window to the front
        window.focus_force()    # Force focus on the window
        set_timer()             # Reset the timer if it goes below 0
    else:
        count_down_after_id=window.after(1000, count_down, seg_time)
        count_min = int(seg_time // 60)
        count_sec = int(seg_time % 60)
        display_time(count_min, count_sec)  # Call the display_time function to update the timer display

def display_time(count_min, count_sec):
    """Update the timer display on the canvas."""
    time_display= f"{count_min if count_min >= 10 else '0' + str(count_min)}:{count_sec if count_sec >= 10 else '0' + str(count_sec)}"
    canvas.itemconfig(timer_text, text=time_display)  # Update the timer display on the canvas

# ---------------------------- UI SETUP ------------------------------- #
import tkinter as tk
window=tk.Tk()
window.config(padx=100, pady=60, bg=YELLOW)  # Set padding and background color
window.title("Pomodoro Timer")
l_timer= tk.Label(text= "Timer", font= (FONT_NAME, 28, "bold"), fg=GREEN, bg=YELLOW)
l_checks= tk.Label(text="", font= (FONT_NAME, 14, "bold"), fg=GREEN, bg=YELLOW)  # Label for check marks

tomato_image= tk.PhotoImage(file=PATH / "tomato.png")  # Load the tomato image from the same directory
canvas=tk.Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
canvas.create_image(100,112,image=tomato_image)
timer_text=canvas.create_text(100,140,text="00:00", font= (FONT_NAME,22,"bold"), fill="white")
b_start= tk.Button(text="Start", highlightthickness=0, command= start_timer)  # Set the command to start the timer
b_reset= tk.Button(text="Reset", highlightthickness=0, command= reset_timer)

b_start.grid(row= 2,column= 0)
b_reset.grid(row=2, column=2)
canvas.grid(row= 1, column= 1, padx=10,pady=10)  # Use grid layout for the canvas
l_timer.grid(row=0, column=1)
l_checks.grid(row=3, column=1)  # Position the label for check marks below the timer
window.mainloop()