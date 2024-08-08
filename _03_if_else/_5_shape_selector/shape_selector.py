import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    geo=turtle.Turtle()
    geo.speed(1)
    geo.color('blue')
    # Ask the user what shape they want to draw and store it in a variable
    shape=simpledialog.askstring(title="Choose your shape", prompt="Would you like to draw a triangle, a square, or a circle? (no capitals)")
    # Draw the shape requested by the user using if-elif-else statements
    if shape=="triangle":
        geo.goto(0,0)
        geo.begin_fill()
        for i in range(3):
            geo.left(120)
            geo.forward(100)
        geo.end_fill()
    elif shape=="square":
        geo.goto(0,0)
        geo.begin_fill()
        for i in range(4):
            geo.right(90)
            geo.forward(100)
        geo.end_fill()
    elif shape=="circle":
        geo.goto(0,0)
        geo.begin_fill()
        geo.circle(radius=50, steps=30)
        geo.end_fill()
    else:
        messagebox.showinfo(message="Invalid Response\n"+"Try again")
    turtle.done()
    # Call the turtle .done() method
