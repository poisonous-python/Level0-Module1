from tkinter import messagebox, simpledialog, Tk
if __name__=='__main__':
    window=Tk()
    window.withdraw()
    today= "08/07"
    bday=simpledialog.askstring(title="Birthday", prompt="What date is your birthday? (mm/dd)")
    if bday==today:
        messagebox.showinfo(message="Happy Birthday to you!")
    else:
        messagebox.showinfo(message="Very Happy UNbirthday to you!")
    window.mainlooop()
