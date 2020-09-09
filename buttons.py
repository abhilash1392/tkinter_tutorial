from tkinter import *

root=Tk()
def myClick():
    myLabel=Label(root,text='I clicked on a button').pack()

# Creating a button
myButton=Button(root,text='Click Me!',padx=50,pady=20,command=myClick)


# Packing it on to the screen
myButton.pack()


# Creating the Loop
root.mainloop()
 