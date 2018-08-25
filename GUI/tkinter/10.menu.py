# Creating a Simple Menu

from tkinter import *

def donothing():
	pass

root=Tk()
root.title('A simple menu')
root.geometry('600x500')

f=Frame(root, height=350, width=300, bg='lightpink')
f.pack()

mb=Menu(root)                     # creating a menu bar
root.config(menu=mb)

filemenu=Menu(root, tearoff=1)
filemenu.add_command(label='New', command=donothing)         #menu items
filemenu.add_command(label='Open', command=donothing)
filemenu.add_command(label='Close', command=donothing)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.destroy)

mb.add_cascade(label='File', menu=filemenu)            # Adding menu items to the File menu

editmenu=Menu(root, tearoff=0)
editmenu.add_command(label='Undo', command=donothing)
editmenu.add_command(label='Cut', command=donothing)
editmenu.add_command(label='Copy', command=donothing)
editmenu.add_command(label='Paste', command=donothing)

mb.add_cascade(label='Edit', menu=editmenu)           # Adding menu items to Edit menu

root.mainloop()

