from tkinter import *

win = Tk()
win.geometry("312x330+700+100")
win.title("Calculator")
win.resizable(False, False)

expression = ""

def bt_clicked(item):
    global expression
    expression = expression + str(item)
    entry.delete(0, END)
    entry.insert(END, expression)

def bt_clear(): 
    global expression 
    expression = "" 
    entry.delete(0, END)

def bt_equal():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, END)
        entry.insert(END, result)
        expression = result  # Store result for further calculations
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

input_frame = Frame(win, width=312, height=50, bd=2)
input_frame.pack(side=TOP)

entry = Entry(input_frame, width=50, font=("arial 18 bold"), bg="grey", bd=2)
entry.grid(row=0, column=0, ipady=10)
entry.focus()

button_frame = Frame(win, height=273, width=312, bg="grey", bd=2)
button_frame.pack()

# Row 1
clear = Button(button_frame, text="AC", fg="black", width=32, height=3, bd=2, bg="grey", cursor="hand2", command=bt_clear)
clear.grid(row=0, column=0, columnspan=3)

divide = Button(button_frame, text="/", fg="black", width=10, height=3, bd=2, bg="grey", cursor="hand2", command=lambda: bt_clicked("/"))
divide.grid(row=0, column=3)

# Row 2
seven = Button(button_frame, text="7", fg="black", width=10, height=3, bd=2, bg="grey", cursor="hand2", command=lambda: bt_clicked(7))
seven.grid(row=1, column=0)

eight = Button(button_frame, text="8", fg="black", width=10, height=3, bd=2, bg="grey", cursor="hand2", command=lambda: bt_clicked(8))
eight.grid(row=1, column=1)

nine = Button(button_frame, text="9", fg="black", width=10, height=3, bd=2, bg="grey", cursor="hand2", command=lambda: bt_clicked(9))
nine.grid(row=1, column=2)

multiply = Button(button_frame, text="X", fg="black", width=10, height=3, bd=2, bg="grey", cursor="hand2", command=lambda: bt_clicked("*"))
multiply.grid(row=1, column=3)

# Row 3
four = Button(button_frame, text="4", fg="black", width=10, height=3, bd=2, bg="grey", cursor="hand2", command=lambda: bt_clicked(4))
four.grid(row=2, column=0)

five = Button(button_frame, text="5", fg="black", width=10, height=3, bd=2, bg="grey", cursor="hand2", command=lambda: bt_clicked(5))
five.grid(row=2, column=1)

six = Button(button_frame, text="6", fg="black", width=10, height=3, bd=2, bg="grey", cursor="hand2", command=lambda: bt_clicked(6))
six.grid(row=2, column=2)

minus = Button(button_frame, text="-", fg="black", width=10, height=3, bd=2, bg="grey", cursor="hand2", command=lambda: bt_clicked("-"))
minus.grid(row=2, column=3)

# Row 4
one = Button(button_frame, text="1", fg="black", width=10, height=3, bd=2, bg="grey", cursor="hand2", command=lambda: bt_clicked(1))
one.grid(row=3, column=0)

two = Button(button_frame, text="2", fg="black", width=10, height=3, bd=2, bg="grey", cursor="hand2", command=lambda: bt_clicked(2))
two.grid(row=3, column=1)

three = Button(button_frame, text="3", fg="black", width=10, height=3, bd=2, bg="grey", cursor="hand2", command=lambda: bt_clicked(3))
three.grid(row=3, column=2)

plus = Button(button_frame, text="+", fg="black", width=10, height=3, bd=2, bg="grey", cursor="hand2", command=lambda: bt_clicked("+"))
plus.grid(row=3, column=3)

# Row 5
zero = Button(button_frame, text="0", fg="black", width=21, height=3, bd=2, bg="grey", cursor="hand2", command=lambda: bt_clicked(0))
zero.grid(row=4, column=0, columnspan=2)

point = Button(button_frame, text=".", fg="black", width=10, height=3, bd=2, bg="grey", cursor="hand2", command=lambda: bt_clicked("."))
point.grid(row=4, column=2)
equal = Button(button_frame, text="=", fg="black", width=10, height=3, bd=2, bg="grey", cursor="hand2", command=lambda: bt_equal())
equal.grid(row=4, column=3)


win.mainloop()
