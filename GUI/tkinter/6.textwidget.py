# Creating a text widget inside root window

from tkinter import *

root=Tk()
root.geometry('600x700')
root.title('Text Widget')

t=Text(root, width=30, height=6, font=('Georgia',25, 'italic'), bg='lightgreen',fg='Purple',wrap=CHAR)

str='''This is a text widget, It is very helpful \n Using text widget we can add\n multiple lines and can edit them'''

t.insert(END,str)     # this will insert the str in textbox
t.pack()

root.mainloop()