import turtle
from Board import *
from time import sleep

playerList = []
playerList.append(Player("black","Alex"))
playerList.append(Player("blue","Ted"))
playerList.append(Player("green","David"))

game = Board(gameSize = 3,players = playerList)
screen = turtle.Screen()
width = 800
height = 800
screen.setup(width+150,height+150)
screen.bgcolor("#dae6da")

drawer = turtle.Turtle()
screen.setworldcoordinates(0,height,width,0)
drawer.color("black")
#drawer.penup()
rows = len(game.board)
columns = len(game.board[0])
spacing = 10
radius = int(min((width - (columns+1)* spacing ) // columns //2, (height*5/6 - (rows+1)* spacing) // rows //2))

#coors  = [[[x,y] for y in range(height//6+ radius,height-radius-spacing+1,2*radius+spacing)] for x in range(spacing+radius,width-spacing-radius+1,2*radius+spacing)]
from itertools import product
coors = []
for i in range(rows):
    y =(height-spacing-100-radius - ((2*radius+spacing)*i))
    a = [[x,y] for x in range(spacing+radius,width-spacing-radius+1,2*radius+spacing)]
    a.reverse()
    coors.extend(a)
coors.reverse()
    
#coors = [[x,y] for x,y in product(range(spacing+radius,width-spacing-radius+1,2*radius+spacing),range( radius+spacing,height-radius-spacing+1,2*radius+spacing))]
turtle.tracer(False)
print(coors)
game.print()
for coor in coors:
    drawer.penup()
    drawer.goto(coor[0],coor[1])
    drawer.pendown()
    drawer.circle(radius)
turtle.update()
def clicker(x,y):
    x = x - spacing
    x = x // (2 * radius+spacing) 
    game.play(int(x))
    if(game.isFinished):
        turtle.done()
def filler(count,color):
    global drawer
    drawer.penup()
    c = turtle.Turtle()
    c.color(color)
    c.penup()
    c.shape("circle")
    c.shapesize(radius/10)
    c.goto(coors[count][0],50)
    turtle.tracer(1)
    c.speed(5)
    c.goto(coors[count])
    c.ht()
    del c
    turtle.tracer(False)
    drawer.goto(coors[count])
    drawer.pendown()
    drawer.color(color)
    drawer.begin_fill()
    drawer.circle(radius)
    drawer.end_fill()
    turtle.update()


##while not game.isFinished:
screen.onclick(clicker)
turtle.mainloop()


    
