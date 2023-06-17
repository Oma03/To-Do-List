"""Description:
Create a command-line-based to-do list application using Python. The application should allow users to add tasks, view
their existing tasks, mark tasks as complete, and remove tasks from the list. You can store the tasks in a text file
 or a simple database."""
# 1. Creating a user interface

import sqlite3
from tkinter import *
td = Tk()
td.title("To-Do-List")


frame1 = LabelFrame(td, padx=5, pady=5)
frame1.pack(padx=10, pady=10)

label1 = Label(frame1, text="TO-DO-LIST", font=("Cambria", 20), fg="white", background="black")
label1.pack()

frame2 = LabelFrame(td, padx=5, pady=5)
frame2.pack(padx=30, pady=30)

button1 = Button(frame2, text="Add Tasks", font=("Cambria", 10))
button1.grid(row=1, column=1)

button2 = Button(frame2, text="View Tasks", font=("Cambria", 10))
button2.grid(row=1, column=2)

button3 = Button(frame2, text="Remove Tasks", font=("Cambria", 10))
button3.grid(row=1, column=3)

mainloop()
