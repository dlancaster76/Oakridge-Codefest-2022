# Importing tkinter module

from tkinter import *
      
import pytesseract as tess
import os
from PIL import Image, ImageTk
from tkinter import * 
from tkinter import Tk
from tkinter import filedialog
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

filename = ''

def browseFiles():
    filename = filedialog.askopenfilename()
    print(filename)

    


  

 
# Creating a tkinter window
root = Tk()           
root.geometry('800x600')    
 

#confirm/photo buttons 
btn1 = Button(root, text = 'Confirm')
btn1.place(x = 325, y = 550)

btn2 = Button(root, text = 'Import Photo', command = browseFiles)
btn2.place(x = 390, y = 550)
 
#image to text test
image = Image.open(filename)
print(tess.image_to_string(image))

image = image.resize((550, 350), Image.ANTIALIAS)


#display image test
image1 = ImageTk.PhotoImage(image)
label1 = Label(root, image = image1)
label1.place(x = 125, y = 100)






root.mainloop()