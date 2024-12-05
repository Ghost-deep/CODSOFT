import string
import random
from tkinter import *

win = Tk()
win.title("Password generator")
win.geometry("400x200")
win.resizable(False, False)
win.config(bg="blue")

m = Frame(win, width=200, height=200, bg="green", bd=4)
m.pack(padx=0, pady=60)

l = Label(m, text="Enter password length : ",bg="green")
l.grid(row=0, column=0)

e = Entry(m,bg="green")
e.focus()
e.grid(row=0, column=1)

def passwordgenrate():
    no = int(e.get())
    a = string.ascii_letters
    b = string.digits
    c = string.punctuation
    l = []
    l.extend(a)
    l.extend(b)
    l.extend(c)
    random.shuffle(l)
    g = "".join(l[0:no])
    e.delete(0, END)
    e.insert(END, g)
    h=Label(m,text="Password Generated Successfully ",bg="green")
    h.grid(row=2,column=1)

a = Button(m, text="Generate", bg="green", command=passwordgenrate)
a.grid(row=0, column=3)

win.mainloop()





