import graphics
from graphics_extra import RoundedRectangle

cor = str(input("Digite a cor para o preenchimento:"))

win = graphics.GraphWin('tk', 1000, 500)
win.setBackground("black")
rect = RoundedRectangle(graphics.Point(100,100),graphics.Point(300, 200),radius=100)
rect.setFill(cor)
rect.setOutline("white")
rect.draw(win)
input("Pressione <enter> para continuar")