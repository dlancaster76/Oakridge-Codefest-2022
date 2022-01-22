from tkinter import *   
 
# create a tkinter window
root = Tk()             
 
root.geometry('500x700')
 
btn = Button(root, text = 'Click me !', bd = '5', command = root.destroy)

 
root.mainloop()