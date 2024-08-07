from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk
window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
color=simpledialog.askstring(title="You're going to help us make a tomato!", prompt="Do you want your tomato to be red, green, or purple?")

# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
if color=="red":
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="black")
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="black")

    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="black")
elif color=="green":
    canvas.create_oval(75, 200, 400, 450, fill="green", outline="black")
    canvas.create_oval(200, 200, 525, 450, fill="green", outline="black")

    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="black")
elif color=="purple":
    canvas.create_oval(75, 200, 400, 450, fill="purple", outline="black")
    canvas.create_oval(200, 200, 525, 450, fill="purple", outline="black")

    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="black")
else:
    messagebox.showinfo(message="Invalid Response. Try Again")
root.mainloop()
