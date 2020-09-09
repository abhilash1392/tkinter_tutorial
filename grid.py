from tkinter import *

root=Tk()
# Creating the Label Widget
myLabel1=Label(root,text='Hello World!')
myLabel2=Label(root,text='My Name is AinzAsta')
myLabel3=Label(root,text='I am a Python Enthusiast')

# Packing it on to the screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=1)
myLabel3.grid(row=2,column=2)


# Creating the Loop
root.mainloop()