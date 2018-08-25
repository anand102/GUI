# Creating a working push button and display output on root window

def display(event):

	lbl= Label(root, text='Hello, I am being clicked', fg='lightpink', bg='yellow', font=('Arial', 20, 'italic'))    # on pressing button, it will print this label
	lbl.pack()
	

from tkinter import *
root=Tk()
root.geometry('750x500')
root.title("Push Button inside Frame")

f=Frame(root, height=300, width=400, bg="lightblue")
f.propagate(0)
f.pack()

b=Button(f, text="Click Me!", width=20, height=2, bg="blue", fg="pink", activebackground="brown", activeforeground="red")
b.pack()
b.bind('<Button-1>',display)     # will call the display function

f.place(x=100,y=100)
b.place(x=80, y=100)
root.mainloop()