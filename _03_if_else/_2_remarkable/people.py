from tkinter import messagebox, simpledialog, Tk
if __name__=='__main__':
    window=Tk()
    window.withdraw()
    name=simpledialog.askstring(title="Name", prompt="What is your name?")
    if name=="Anagha":
        messagebox.showinfo(message="Anagha likes to dance")
    elif name=="Bob":
        messagebox.showinfo(message="Bob likes to rollerskate")
    elif name=="Jeff":
        messagebox.showinfo(message="Jeff likes to cook\n"+"(although he's not very good at it)")
    else:
        messagebox.showinfo(message="Welcome to the league, "+name+"! What's one cool fact about you?")
        cool=simpledialog.askstring(title=name+"'s cool fact", prompt="What's one cool fact about you?")
        messagebox.showinfo(message="Wow "+name+"! That's pretty cool!")
        messagebox.showinfo(message="Adding to file...\n"+name+"'s cool fact:\n"+"'"+cool+"'")
