import tkinter as tk
from tkinter import ttk

counter = 0
def mouse_click(event):
    global counter
    counter = counter + 3
    print(counter)

windows = tk.Tk()
label = tk.ttk.Button(windows, text="Click here!")
label.pack()
label.bind("<Triple-Button>", mouse_click)
label.grid(column=1, row=0)
windows.mainloop()