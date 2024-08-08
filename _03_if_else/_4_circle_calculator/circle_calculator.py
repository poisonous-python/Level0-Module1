from tkinter import messagebox, simpledialog, Tk
import math
# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr

if __name__ =='__main__':
    window=Tk()
    window.withdraw()
    r=simpledialog.askinteger(title= "Your Circle", prompt="What would you like the radius of your circle to be? (no labels, only number)")
    calc=simpledialog.askstring(title="Choose your calculation", prompt="Would you like to calculate the circumference or the area of your circle? (please capitalize)")
    if calc=="Area":
        messagebox.showinfo(message="Calculating...\n"+"Click 'Okay' to continue")
        a=math.pi*r*r
        messagebox.showinfo(message="The area of your circle is "+str(a))
    elif calc=="Circumference":
        messagebox.showinfo(message="Calculating...\n"+"Click 'Okay' to continue")
        c=2*math.pi*r
        messagebox.showinfo(message="The circumference fo your circle is "+str(c))
    else:
        messagebox.showinfo(message="Invalid response\n"+"Try Again\n"+"(Remember to capitalize)")
