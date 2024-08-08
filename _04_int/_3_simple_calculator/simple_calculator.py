from tkinter import messagebox, simpledialog, Tk
import math
"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
if __name__=='__main__':
    window=Tk()
    window.withdraw()
    nam=simpledialog.askstring(title="Your name", prompt="What is your name?")
    messagebox.showinfo(message="Welcome "+nam+"! Are you ready to do some math?")
    num1=simpledialog.askinteger(title=nam+"'s First Number", prompt="Choose a number "+nam+"!")
    num2=simpledialog.askinteger(title=nam+"'s Second Number", prompt="Great! now choose a different number, then you'll decide what to do with them!")
    choice=simpledialog.askstring(title=nam+"'s Decision", prompt="Now, would you like to add, subtract, multiply, or divide your two numbers? (please don't capitalize)")
    if choice=="add":
        add=num1+num2
        messagebox.showinfo(message="Excellent choice, "+nam+"!\n"+"Your sum is:\n"+str(add))
    elif choice=="subtract":
        subtract=num1-num2
        messagebox.showinfo(message="Excellent choice, "+ nam+"!\n"+"Your difference is:\n"+str(subtract))
    elif choice=="multiply":
        multiply=num1*num2
        messagebox.showinfo(message="Excellent choice, "+ nam+"!\n"+"Your new number is:\n"+str(multiply))
    elif choice=="divide":
        divide=num1/num2
        messagebox.showinfo(message="Excellent choice, "+ nam+"!\n"+"Your new number is:\n"+str(divide))
    else:
        messagebox.showinfo(message="Uh Oh! Something went wrong, try again. Remember, no capitals!")
    window.mainloop
