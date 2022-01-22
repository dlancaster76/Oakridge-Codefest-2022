# Importing tkinter module

from tkinter import *
import pytesseract as tess
import os
from PIL import Image, ImageTk
from tkinter import Tk
from tkinter import filedialog
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


    


  

 
# Creating a tkinter window
root = Tk()           
root.geometry('800x600')   

def return_dir():
    global my_image
    root.filename = filedialog.askopenfilename()
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()
    btn2.destroy()
    
def image2text():
    text = tess.image_to_string(root.filename)
    print(text)

#confirm/photo buttons 
btn1 = Button(root, text = 'Confirm', command=image2text)
btn1.place(x = 325, y = 550)

btn2 = Button(root, text = 'Import Photo', command=return_dir)
btn2.place(x = 390, y = 550)
 







root.mainloop()