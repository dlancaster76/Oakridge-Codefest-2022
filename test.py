# Importing tkinter module
from fileinput import filename
from tkinter import *       
import pytesseract as tess
import os
import subprocess
from PIL import Image, ImageTk
from tkinter import Tk 
from tkinter.filedialog import askopenfilename
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


filename = askopenfilename()
if filename.endswith(".jpg") or filename.endswith('.png'):
    print(filename)


