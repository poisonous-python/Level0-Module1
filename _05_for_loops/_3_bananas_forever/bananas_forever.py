from tkinter import messagebox, simpledialog, Tk
"""
 * Write a python program that prints the word 'banana' one thousand (1,000) times
"""
if __name__=='__main__':
    window=Tk()
    window.withdraw()
    for i in range(1000):
        print("BANANA")
window.mainloop()
