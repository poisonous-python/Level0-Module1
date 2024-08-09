from tkinter import messagebox, simpledialog, Tk
if __name__=='__main__':
    window=Tk()
    window.withdraw()
    for i in range(14):
        messagebox.showinfo(message="in "+str(i+2010)+", I  was "+str(i)+ " years old.")
        print(str(i))
window.mainloop()
