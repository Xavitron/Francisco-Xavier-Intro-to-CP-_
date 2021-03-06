#Sources
''' https://stackoverflow.com/questions/45093430/tron-game-collision-turtle-python
    https://stackoverflow.com/a/9997374/5771269
    myNineth,py  
'''
import turtle
from turtle import Turtle, Screen
from turtle import *
from random import randint 

mypen = Turtle()
player = Turtle()
constantSpeed = player.speed(15)
screen = Screen()
#screen = turtle.Screen()
bgTurtle = Turtle()
screenTurtle = bgTurtle.getscreen()
screenTurtle.bgpic("background.gif")
    
    
#Changes background color to black
#screen.setup(1600,1000)
#screen.bgcolor("black")
#screen.bgpic("background.gif")
#screen.bgpic("C:/Users/X.MendiburuPerez20/OneDrive - Bellarmine College Preparatory/Intro_to_CP/Mendiburu_Xavi/Final Project/background.jpg")

#Draw border of the game 
mypen.penup()
mypen.speed(10)
mypen.hideturtle()
mypen.color("yellow")
mypen.pensize(3)
mypen.forward(300)
mypen.pendown()
mypen.left(90)
mypen.forward(300)
mypen.color("lightgreen")
mypen.left(90)
mypen.forward(300)
mypen.color("yellow")
mypen.forward(300)
mypen.color("lightgreen")
mypen.left(90)
mypen.forward(300)
mypen.color("yellow")
mypen.forward(300)
mypen.color("lightgreen")
mypen.left(90)
mypen.forward(300)
mypen.color("yellow")
mypen.forward(300)
mypen.color("lightgreen")
mypen.left(90)
mypen.forward(300)
screen.title("Python Turtle game with classes...")
dead = False

#It tells the turtle that when the user tells them to move up, the player or the enemy will move up depending on the key that is pressed
def up(who):
    global previousMove

    turtle, path = players[who]
    turtle.setheading(90)

    if previousMove != 'up':
        path.append(turtle.position())
    previousMove = 'up'

    turtle.fd(15)
#here it checks if the you have collided before making the next move
    if checkCollision(turtle.position(), path, players[1 - who][PATH]):
        collision(turtle)

#It tells the turtle that when the user tells them to move to the right, the player or the enemy will move to the right depending on the key that is pressed
def right(who):
    global previousMove

    turtle, path = players[who]
    turtle.setheading(0)

    if previousMove != 'right':
        path.append(turtle.position())
    previousMove = 'right'

    turtle.fd(15)
#here it checks if the you have collided before making the next move
    if checkCollision(turtle.position(), path, players[1 - who][PATH]):
        collision(turtle)

#It tells the turtle that when the user tells them to move to the left, the player or the enemy will move to the left depending on the key that is pressed
def left(who):
    global previousMove

    turtle, path = players[who]
    turtle.setheading(180)

    if previousMove != 'left':
        path.append(turtle.position())
    previousMove = 'left'

    turtle.fd(15)
#here it checks if the you have collided before making the next move
    if checkCollision(turtle.position(), path, players[1 - who][PATH]):
        collision(turtle)

#It tells the turtle that when the user tells them to move down, the player or the enemy will move down depending on the key that is pressed
def down(who):
    global previousMove

    turtle, path = players[who]
    turtle.setheading(270)

    if previousMove != 'down':
        path.append(turtle.position())
    previousMove = 'down'

    turtle.fd(15)
#here it checks if the you have collided before making the next move
    if checkCollision(turtle.position(), path, players[1 - who][PATH]):
        collision(turtle)

#This makes the turtles stop when one turtle crosses the others line 
def collision(turtle):
    for key in ('Up', 'Left', 'Right', 'Down', 'w', 'a', 'd', 's'):
        screen.onkey(None, key)  # disable game
    turtle.clear()  # remove the loser from the board!

def checkCollision(position, path1, path2):
    if len(path1) > 1:

        A, B = position, path1[-1]  # only check most recent line segment

        if len(path1) > 3:  # check for self intersection
            for i in range(len(path1) - 3):
                C, D = path1[i:i + 2]

                if intersect(A, B, C, D):
                    return True

        if len(path2) > 1:  # check for intersection with other turtle's path
            for i in range(len(path2) - 1):
                C, D = path2[i:i + 2]

                if intersect(A, B, C, D):
                    return True
    return False

X, Y = 0, 1

def ccw(A, B, C):
    """ https://stackoverflow.com/a/9997374/5771269 """
    return (C[Y] - A[Y]) * (B[X] - A[X]) > (B[Y] - A[Y]) * (C[X] - A[X])

def intersect(A, B, C, D):
    """ Return true if line segments AB and CD intersect """
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

#Here youre creating a player 
player = Turtle('circle')
player.speed(1)
player.shapesize(6 / 20)
player.color('red')
player.pensize(6)
player.speed('fastest')
player.penup()
player.setposition(100, 100)
player.pendown()
#Here you create an enemy 
enemy = Turtle('circle')
player.speed(1)
enemy.shapesize(6 / 20)
enemy.color('blue')
enemy.pensize(6)
enemy.speed('fastest')
enemy.penup()
enemy.setposition(-100, -100)
enemy.pendown()

players = [[player, [player.position()]], [enemy, [enemy.position()]]]
PLAYER, ENEMY = 0, 1
TURTLE, PATH = 0, 1

previousMove = None  # consolidate moves in same direction into single line segment

screen.onkey(lambda: up(PLAYER), 'Up')
screen.onkey(lambda: left(PLAYER), 'Left')
screen.onkey(lambda: right(PLAYER), 'Right')
screen.onkey(lambda: down(PLAYER), 'Down')

screen.onkey(lambda: up(ENEMY), 'w')
screen.onkey(lambda: left(ENEMY), 'a')
screen.onkey(lambda: right(ENEMY), 'd')
screen.onkey(lambda: down(ENEMY), 's')

#Boundary check for player 
if player.pos()[0] > 300 or player.pos()[0] < -300:
    print("Game Over")
    quit()
if player.pos()[1] > 300 or player.pos()[1] < -300:
    print("Game OVer")
    quit()

#Boundary check for enemy
if enemy.pos()[0] > 300 or enemy.pos()[0] < -300:
    print("Game Over")
    quit()
if enemy.pos()[1] > 300 or enemy.pos()[1] < -300:
    print("Game Over")
    quit()

  

screen.listen()

screen.mainloop()