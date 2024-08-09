from tkinter import *

window_width = 800
window_height = 800
root = Tk()

canvas = Canvas(root, width=window_width, height=window_height, borderwidth=0, highlightthickness=0, bg="#000050")
canvas.grid()


# This code runs whenever the mouse is clicked on the window
def mouse_pressed(event):
    # Draws a dark blue background
    canvas.create_rectangle(0, 0, window_width, window_height, fill="#000050")

    # x and y will be equal to the mouse pointer's x and y location
    x = event.x
    y = event.y
    
    # This defines the x and y coordinated of all three points
    # of a triangle
    points = [x, y, x - 50, y + 100, x + 50, y + 100]
    canvas.create_polygon(points, fill='gray', width=2) # draws triangle
    recpoints= [x+50, y+100, x-50, y+400]
    canvas.create_rectangle(recpoints, fill='gray', width=2)
    cirpts=[x-80, y+400, x+80, y+560]
    canvas.create_oval(cirpts, fill='red', width=2)
    smcpts=[x-60, y+400, x+60, y+520]
    canvas.create_oval(smcpts, fill='orange', width=2)
    ycir=[x-40, y+410, x+40, y+490]
    canvas.create_oval(ycir, fill='yellow', width=2)
    hexpts= [x-50, y+400, x+50, y+400,  x+90, y+470, x-90, y+470]
    canvas.create_polygon(hexpts, fill='gray', width=2)
    # 1. Add details to your rocket to make it look better. You can look at
    #    rocket.png for inspiration.
    
    # 2. Modify the locations of the shapes above so the rocket will be drawn
    #    where the mouse is clicked
    

# ====================== DO NOT MODIFY THE CODE BELOW ========================

canvas.bind("<Button-1>", mouse_pressed)

root.mainloop()
