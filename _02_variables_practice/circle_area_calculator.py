import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    rad=simpledialog.askinteger(title="Let's make a cirlce!", prompt="What's the radius of your circle? (no labels)")
    
    # Make a new turtle
    circly=turtle.Turtle()
    circly.speed(10)
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    circly.circle(radius=rad, steps=30)
    # Call the turtle .penup() method
    circly.penup()
    # Move your turtle to a new x,y position using .goto()
    circly.goto(0, 5)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    a=math.pi*rad*2
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    circly.write(arg="area= "+ str(a), move=True, align='left', font=('Arial', 15, 'normal'))
    # Hide your turtle
    circly.hideturtle()
    # Call turtle.done()
    turtle.done()
