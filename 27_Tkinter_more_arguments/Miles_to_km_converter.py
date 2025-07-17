import tkinter as tk
window = tk.Tk()
window.title("Miles to km converter")
window.config(padx=20, pady=20)

def miles_to_km():
    km= float(entry.get()) * 1.609
    l_total.config(text=str(round(km,2)))



entry= tk.Entry(window, width=15)
entry.grid(row=0, column=1)
l_miles=tk.Label(window, text="Miles")
l_km=tk.Label(window, text="Km")
l_isequalto=tk.Label(window, text="Is equal to: ")
l_total=tk.Label(window, text="0")
button=tk.Button(window, text="Calculate", command= miles_to_km)

l_miles.grid(row=0, column=2)
l_km.grid(row=1, column=2)
l_isequalto.grid(row=1, column=0)
button.grid(row=2, column=1)
entry.grid(row=0, column=1)
l_total.grid(row=1, column=1)
window.mainloop()