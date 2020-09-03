import random
import math
import os
from tkinter import Tk, Canvas, PhotoImage, mainloop

os.system('cls')

def executar():
    mainloop()

def writePixel(x,y,color):
    img.put(color, (x,y))

def circlePoints(x,y,largura,altura,color):
    writePixel(largura + x,altura + y,color)
    writePixel(largura + x,altura - y,color)
    writePixel(largura - x,altura + y,color)
    writePixel(largura - x,altura - y,color)
    writePixel(largura + y,altura + x,color)
    writePixel(largura + y,altura - x,color)
    writePixel(largura - y,altura + x,color)
    writePixel(largura - y,altura - x,color)

def elipsePoints(x,y,largura,altura,color):
    writePixel(largura + x,altura + y,color)
    writePixel(largura - x,altura - y,color)    
    writePixel(largura + x,altura - y,color)
    writePixel(largura - x,altura + y,color)

def drawLine(x1,y1,x2,y2,color):
    dx = x2 - x1
    dy = y2 - y1
    d  = (dy * 2) - dx
    incrE = dy * 2 
    incrNE = (dy - dx) * 2
    x = x1 
    y = y1 
    writePixel(x,y,color)

    if (x == x2) and (y != y2):
        if y > y2:
            diferenca = y - y2
            menor = y2
        elif y < y2:
            diferenca = y2 - y
            menor = y

        for i in range(0,diferenca,1):
            writePixel(x,menor + i,color)

    while (x < x2):
        if d <= 0 : 
            d += incrE
            x += 1
        else: 
            d += incrNE
            x += 1
            y += 1
            
        writePixel(x,y,color)
    
    while (x > x2):
        if d <= 0 : 
            d -= incrE
            x -= 1
        else: 
            d -= incrNE
            x -= 1
            y -= 1
            
        writePixel(x,y,color)

def drawCircle(raio,largura,altura,color):
    x = 0
    y = raio
    d = 1 - raio
    circlePoints(x,y,largura,altura,color)

    while (y > x):
        if (d < 0):
            d = d + (2 * x) + 3
            x += 1
        else:
            d = d + (2 * (x - y)) + 5
            x += 1
            y -= 1
            
        circlePoints(x,y,largura,altura,color)

def drawElipse(a,b,largura,altura,color):
    x = 0
    y = b
    p1 = (b * b) - (a * a * b) + ((a * a) * 0.25)
    elipsePoints(x,y,largura,altura,color)

    while (((a * a) * (y - 0.5)) > ((b * b) * (x + 1))):
        if (p1 < 0):
            p1 += (b * b) + ((2 * x) + 3)
        else:
            p1 += ((b * b) + ((2 * x) + 3)) + ((a * a) - ((-2 * y) + 2))
            y  -= 1        

        x += 1  
        elipsePoints(x,y,largura,altura,color)

    p2 =((b * b) * ((x + 0.5) * (x + 0.5))) + ((a * a) * ((y - 1) * (y - 1))) - ((a * a) * (b * b))
    while (y > 0):
        if (p2 < 0):
            p2 += ((b * b) * ((2 * x) + 2)) + ((a * a) * ((-2 * y) + 3))
            x  += 1
        else:  
            p2 += (a * a) * ((-2 * y) + 3)

        y -= 1
        elipsePoints(x,y,largura,altura,color)

largura = 1000
altura  = 500
window = Tk()
canvas = Canvas(window, width=largura, height=altura, bg="#000000")
canvas.pack()
img = PhotoImage(width=largura, height=altura)
canvas.create_image((largura//2, altura//2), image=img, state="normal")

loop = True

while loop:
    print("\nEscolha uma opção abaixo:")
    print("""1 - Segmento de Reto
2 - Circulo 
3 - Elipse """)
    escolha = int(input())

    if escolha == 1:
        drawLine(100,100,500,100,"#ffffff")
    elif escolha == 2:
        drawCircle(149,largura//2,altura//2,"#ffffff")
    else:
        drawElipse(20,200,largura//2,altura//2,"#ffffff")
    
    executar()

    print("""
Deseja Continuar?
1 - Sim
2 - Não""")
    escolha = int(input())
    
    if escolha == 2:
        loop = False
    else:
        largura = 1000
        altura  = 500
        window = Tk()
        canvas = Canvas(window, width=largura, height=altura, bg="#000000")
        canvas.pack()
        img = PhotoImage(width=largura, height=altura)
        canvas.create_image((largura//2, altura//2), image=img, state="normal")