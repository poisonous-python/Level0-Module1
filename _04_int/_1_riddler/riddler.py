from tkinter import messagebox, simpledialog, Tk
"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
if __name__=='__main__':
    window=Tk()
    window.withdraw()
    score=0
    r1=simpledialog.askstring(title="Riddle 1/3", prompt="What has a mouth, but never eats, has a bed, but never sleeps, and runs but never walks? (no capitals, one word only)")
    if r1=="river":
        score+=1
        messagebox.showinfo(message="Correct!\n"+"+1 point")
    else:
        score-=1
        messagebox.showinfo(message="Incorrect!\n"+"-1 point\n"+"Correct Answer: river")
    r2=simpledialog.askstring(title="Riddle 2/3", prompt="The more you take, the more you leave behind. What am I? (one word, no capitals)")
    if r2=="footsteps":
        score+=1
        messagebox.showinfo(message="Correct!\n"+"+1 point")
    else:
        score-=1
        messagebox.showinfo(message="Incorrect!\n"+"-1 point\n"+"Correct Answer: footsteps")
    r3=simpledialog.askstring(title="riddle 3/3", prompt="What starts with the letter e, ends with the letter e, contains only one letter, but is not the letter e?(one word, no capitals)")
    if r3=="envelope":
         score+=1
         messagebox.showinfo(message="Correct!\n"+"+1 point")
    else:
        score-=1
        messagebox.showinfo(message="Incorrect!\n"+"-1 point\n"+"Correct Answer: envelope")
    r4=simpledialog.askstring(title="Bonus Riddle!", prompt="What belongs to me, but is used more by others than by me? (no capitals)\n"+"This is worth 3 points!")
    if r4=="your name":
         score+=3
         messagebox.showinfo(message="Correct! Wow!\n"+"+1 point")
    else:
         messagebox.showinfo(message="Incorrect!\n"+"No penalty\n"+"Correct Answer: your name")
    messagebox.showinfo(message="Your score is "+str(score)+"/6!\n"+"Good Job!")
    window.mainloop()
