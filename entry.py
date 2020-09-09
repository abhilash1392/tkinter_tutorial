from tkinter import *


root=Tk()

e=Entry(root,width=50,bg='blue',fg='white',borderwidth=(5))
e.pack()
e.insert(0,'Enter Your Name')
def myClick():
    hello='Hello ' + e.get()
    
    myLabel=Label(root,text=hello).pack()

# Creating a button
myButton=Button(root,text='Enter Your Name',padx=50,pady=20,command=myClick)


# Packing it on to the screen 
myButton.pack()


# Creating the Loop
root.mainloop()

