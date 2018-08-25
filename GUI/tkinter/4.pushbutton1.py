# Creating a working push button

def display(event):
    print("Hey, You Clikced the button")


from tkinter import *
root=Tk()
root.geometry('750x500')
root.title("Push Button inside Frame")

f=Frame(root, height=300, width=400, bg="lightblue")
f.propagate(0)
f.pack()

b=Button(f, text="Click Me!", width=20, height=2, bg="blue", fg="pink", activebackground="brown", activeforeground="yellow")
b.pack()
b.bind('<Button-1>',display)     #this will call display function and gies output on DOS, button-1 means left click of mouse

f.place(x=100,y=100)
b.place(x=80, y=100)
root.mainloop()