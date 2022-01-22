# Importing tkinter module
from tkinter import *       
 
# Creating a tkinter window
root = Tk()           
root.geometry('500x750')    
 
btn = Button(root, text = 'Click me !', command = root.destroy)
btn.place(x=225, y=375)
 
root.mainloop()