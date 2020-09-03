import random
import math

from tkinter import * 
from tkinter import messagebox as tkMessageBox

class Graphics:
    def __init__(self,largura,altura,cor):
        self.largura = largura
        self.altura  = altura
        self.cor     = cor
        self.window  = Tk()
        self.canvas  = Canvas(self.window, width=largura, height=altura, bg="#000000")
        self.canvas.pack()

    def executar(self):
        self.window.protocol("WM_DELETE_WINDOW", self.next)
        mainloop()
        
    def next(self):
        if tkMessageBox.askokcancel("Sair", "Você realmente deseja sair ?"):
            self.window.destroy()

    def drawLine(self,x1,y1,x2,y2):
        self.canvas.create_line(x1,y1,x2,y2,fill = self.cor)

    def drawRect(self,x1,y1,x2,y2):
        self.canvas.create_rectangle(x1,y1,x2,y2,outline = "white",fill = self.cor)

    def drawOval(self,x1,y1,x2,y2):
        self.canvas.create_oval(x1,y1,x2,y2,outline = "white",fill = self.cor)
        
    def drawPolygon(self,x1,y1,x2,y2,x3,y3):
        self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,outline = "white",fill = self.cor)