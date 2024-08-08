from tkinter import messagebox, simpledialog, Tk
import math
"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
if __name__=='__main__':
    window=Tk()
    window.withdraw()
    name=simpledialog.askstring(title="Your name", prompt="What is your name?")
    no1=simpledialog.askinteger(title=name+"'s first number", prompt="Choose a number (any number)")
    no2=simpledialog.askinteger(title=name+"'s second number", prompt="Choose a different number(any OTHER number)")
    sum=no1+no2
    messagebox.showinfo(message="Calculating...\n"+"Press OK to find the sum of your two numbers")
    messagebox.showinfo(message=name+"'s sum:\n"+"Your sum is:"+str(sum))
    window.mainloop
