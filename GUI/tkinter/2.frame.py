# creating a frame inside root window

from tkinter import *
root=Tk()
root.title("My Frame")
root.geometry('600x500')

f=Frame(root, height=300 ,width=300 , bg="yellow")
f.pack()

root.mainloop()