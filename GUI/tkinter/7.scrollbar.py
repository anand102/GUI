# Making a scrollbar along with text widget

from tkinter import *

root=Tk()
root.geometry('600x700')
root.title('Text Widget')



t=Text(root, width=30, height=6, font=('Georgia',25, 'italic'), bg='lightgreen',fg='Purple',wrap=CHAR)

str='''This is a text widget, It is very helpful \n Using text widget we can add\n multiple lines and can edit them'''

t.insert(END,str)    
t.pack()

s= Scrollbar(root, orient=VERTICAL, command=t.yview)       #scrollbar added in root in vertical , y.view states its on y axis
t.configure(yscrollcommand= s.set)                # configure scrolbar with text widget
s.pack(side=RIGHT, fill=Y)            # right side of window

root.mainloop()