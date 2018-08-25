# Creating Labels and Entry Boxes

def display(event):
	name=e1.get()
	pwd= e2.get()
	
	lbl= Label(f, text=name+pwd,width=30)
	lbl.place(x=10, y=140)

from tkinter import *

root=Tk()

root.title("Entry boxes with lables")
root.geometry('600x450')

f=Frame(root, height=300, width=380)
f.pack()

l1=Label(f, text='Enter your name: ')
l2=Label(f, text='Enter Password: ')

e1= Entry(f, width=25, bg='lightblue', fg='Purple', font=('Geopardy', 15, 'italic'))
e2= Entry(f, width=25, bg='lightblue', fg='Purple', font=('Geopardy', 15, 'italic'), show='*')

e2.bind('<Return>',display)
l1.place(x=50, y=50)
l2.place(x=50, y=100)

e1.place(x=150, y=50)
e2.place(x=150, y=100)


root.mainloop()