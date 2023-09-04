# calculator application for python

# import tkinter module
from tkinter import *

# create a window
root = Tk()

# set window title
root.title("Calculator")

# set window size
root.geometry("400x400")

# set window background color
root.config(bg="light green")

# create a label for the calculator
label = Label(root, text="Calculator", font=("Arial", 20, "bold"), bg="light green")
label.pack()

# create a text entry box
entry = Entry(root, font=("Arial", 20, "bold"), bg="light green")
entry.pack()

# create a frame for the buttons
frame = Frame(root)
frame.pack()

# create a function to add numbers
def add():
    global operator
    operator = "+"
    global first_number
    first_number = entry.get()
    entry.delete(0, END)

# create a function to subtract numbers
def subtract():
    global operator
    operator = "-"
    global first_number
    first_number = entry.get()
    entry.delete(0, END)

# create a function to multiply numbers
def multiply():
    global operator
    operator = "*"
    global first_number
    first_number = entry.get()
    entry.delete(0, END)

# create a function to divide numbers
def divide():
    global operator
    operator = "/"
    global first_number
    first_number = entry.get()
    entry.delete(0, END)

# create a function to calculate the answer
def equal():
    second_number = entry.get()
    entry.delete(0, END)
    if operator == "+":
        entry.insert(0, float(first_number) + float(second_number))
    elif operator == "-":
        entry.insert(0, float(first_number) - float(second_number))
    elif operator == "*":
        entry.insert(0, float(first_number) * float(second_number))
    elif operator == "/":
        entry.insert(0, float(first_number) / float(second_number))

# create a function to clear the screen
def clear():
    entry.delete(0, END)

# create a button for the add function
add_button = Button(frame, text="+", font=("Arial", 20, "bold"), bg="light green", command=add)
add_button.grid(row=0, column=0)

# create a button for the subtract function
subtract_button = Button(frame, text="-", font=("Arial", 20, "bold"), bg="light green", command=subtract)
subtract_button.grid(row=0, column=1)

# create a button for the multiply function
multiply_button = Button(frame, text="*", font=("Arial", 20, "bold"), bg="light green", command=multiply)
multiply_button.grid(row=1, column=0)

# create a button for the divide function
divide_button = Button(frame, text="/", font=("Arial", 20, "bold"), bg="light green", command=divide)
divide_button.grid(row=1, column=1)

# create a button for the equal function
equal_button = Button(frame, text="=", font=("Arial", 20, "bold"), bg="light green", command=equal)
equal_button.grid(row=2, column=0)

# create a button for the clear function
clear_button = Button(frame, text="C", font=("Arial", 20, "bold"), bg="light green", command=clear)
clear_button.grid(row=2, column=1)

# run the main loop
root.mainloop()

# end of program