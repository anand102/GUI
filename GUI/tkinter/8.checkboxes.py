# Creating CheckBoxes

from tkinter import *

def display():
	x=var1.get()
	y=var2.get()
	z=var3.get()

	str=''
	if x==1 : str+='Python'
	if y==1 : str+='JAVA'
	if z==1 : str+= '.NET'

	lbl=Label(f, text=str, width=20)
	lbl.place(x=100, y=300)



root=Tk()
root.title("Checkboxes")
f= Frame(root, height= 500, width=600, bg="lightpink")
f.pack()

var1=IntVar()
var2=IntVar()
var3=IntVar()

c1=Checkbutton(f, bg='lightblue', fg='blue', font=('Arial', 20, 'italic'), text="Python", variable=var1, command=display)
c2=Checkbutton(f, bg='lightblue', fg='blue', font=('Arial', 20, 'italic'), text="JAVA", variable=var2, command=display)
c3=Checkbutton(f, bg='lightblue', fg='blue', font=('Arial', 20, 'italic'), text=".NET", variable=var3, command=display)

c1.place(x=100,y=50)
c2.place(x=100,y=150)
c3.place(x=100,y=250)

root.mainloop()