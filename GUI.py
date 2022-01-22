# Importing tkinter module
from tkinter import *       
import pytesseract as tess
import os
from PIL import Image, ImageTk
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
 
# Creating a tkinter window
root = Tk()           
root.geometry('800x650')    
 

#confirm/photo buttons 
btn1 = Button(root, text = 'Confirm')
btn1.place(x = 325, y = 600)

btn2 = Button(root, text = 'Import Photo')
btn2.place(x = 390, y = 600)
 
#image to text test
image = Image.open('text1.png')
print(tess.image_to_string(image))

image = image.resize((550, 350), Image.ANTIALIAS)


#display image test
image1 = ImageTk.PhotoImage(image)
label1 = Label(root, image = image1)
label1.place(x = 125, y = 100)




root.mainloop()