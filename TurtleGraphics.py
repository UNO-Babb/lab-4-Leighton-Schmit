#TurtleGraphics.py
#Name: Leighton Schmit
#Date: 9/18/24
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def drawPolygon(joe, sides):
    for i in range(sides):
        joe.forward(50)
        joe.right(360 / sides)

def fillCorner(myTurtle,corner):
    myTurtle = turtle.Turtle()
    drawSquare(myTurtle, 100)
    
    if corner == 2:
        myTurtle.forward(50)
    elif corner == 3:
        myTurtle.right(90)
        myTurtle.forward(50)
        myTurtle.left(90)
    elif corner == 4:
        myTurtle.up()
        myTurtle.goto(100, -100)
        myTurtle.down()
        myTurtle.right(180)
    else:
        myTurtle.right(0)
    myTurtle.begin_fill()
    drawSquare(myTurtle, 50)
    myTurtle.end_fill()
#def squaresInSquares(myTurtle, num):
    #size = 10
    #for i in range(num):
        #drawSquare(myTurtle, size)
        #size = size + 20
        #myTurtle.up()
        #

def main():
    myTurtle = turtle.Turtle()
    #drawSquare(myTurtle, 50)
    #drawPolygon(myTurtle, 6) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    

    
#for i in range(1, 15, 1):
    #myTurtle = turtle.Turtle()
    #drawPolygon(myTurtle, i)

    fillCorner(myTurtle, 4) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
