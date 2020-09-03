from Classes.Graphics import Graphics

cor = str(input("Digite a cor para o preenchimento:"))

g = Graphics(1000,500,cor)
g.drawLine(10,10,10,200)
g.drawRect(50,200,150,350)
g.drawOval(200,100,500,150)
g.drawPolygon(20,50,40,40,100,150)
g.executar()