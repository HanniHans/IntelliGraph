from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Datos files","*.csv"),("all files","*.*")))
print (root.filename) #ruta del archivo