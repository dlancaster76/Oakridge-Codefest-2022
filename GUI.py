# Importing tkinter module
from tkinter import *       
import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
 
# Creating a tkinter window
root = Tk()           
root.geometry('500x750')    

#confirm/photo buttons 
btn1 = Button(root, text = 'Confirm')
btn1.place(x=150, y=600)

btn2 = Button(root, text = 'Import Photo')
btn2.place(x=215, y=600)
 
#image to text test
img = Image.open('text1.png')
print(tess.image_to_string(img))

#display image test



root.mainloop()