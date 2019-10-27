#from tkinter import *
#raiz=Tk()
#raiz.title("Venta de pruebas")
#raiz.resizable(0,0)
#raiz.iconbitmap()
#raiz.geometry("750x400")
#raiz.config(bg="white")
#raiz.mainloop()


#mi frame.pack()

import tkinter as tk
from tkinter import *
from tkinter import ttk

class inicio( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("IntelliGraph")
        self.config(width="750", height="400")
        self.abrir = Button(self, text = "Abrir Archivo", width = 25,command = self.new_window)
        #self.button1 = Button( self, text = "CLICK HERE", width = 25,
                              # command = self.new_window )
        #self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
    def new_window(self):
        self.newWindow = karl2()


def main(): 
    inicio().mainloop()
if __name__ == '__main__':
    main()