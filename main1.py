#My project is going to be something similar to the game lightbikes from tron the movie
#My first major milestone, is to set the boundaries of the area were the bikes run in
#I do not know how to insert images in python, I know we have learned how to do it, but I forgot about them
#I do not think my project is too ambitious
#I think maybe my project is too easy to do.
import turtle
from turtle import Turtle, Screen
import random 

WITH, Height = 1000,1000
mypen = Turtle()
wn = turtle.Screen()
previousMove = "na" 

#Change background color 
wn.bgcolor("black")

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

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Python Turtle game with classes...")
dead = False

#Player 1 class
class Player1(Turtle):

    def __init__(self, left, right, speedup, slowdown):
        Turtle.__init__(self)
        self.pendown()
        self.speed(0)
        self.pensize(10)
        self.shape("triangle")
        self.color("blue")
        self.currentSpeed = 1
        self.leftTurn = left
        self.rightTurn = right
        self.speedup = speedup
        self.slowdown = slowdown
        self.pos()
    def turnLeft(self):
        self.left(90)
        print("turning left")
    def turnRight(self):
        self.right(90)
        print("turning right")         
    def move(self):
        self.forward(self.currentSpeed)
        self.screen.listen()
        wn.onkeypress(self.turnLeft, self.leftTurn)
        wn.onkeypress(self.turnRight, self.rightTurn)
        wn.onkeypress(self.increaseSpeed, self.speedup) 
        wn.onkeypress(self.decreaseSpeed, self.slowdown)    

        
    def increaseSpeed(self):
        self.currentSpeed += 1

    def decreaseSpeed(self):
        self.currentSpeed -= 1



#Player2 class

class Player2(Turtle):

    def __init__(self, left, right, speedup, slowdown):
        Turtle.__init__(self)
        self.pendown()
        self.speed(0)
        self.pensize(10)
        self.shape("circle")
        self.color("red")
        self.currentSpeed = 1
        self.leftTurn = left
        self.rightTurn = right
        self.speedup = speedup
        self.slowdown = slowdown
        self.pos()
    def turnLeft(self):
        self.left(90)
        print("turning left")
    def turnRight(self):
        global previousMove 

        turtle,path = players[self]
        self.right(90)
        if previousMove != "rightTurn":
            path.append(turtle.position())
            previousMove = "rightTurn"
        if checkCollision(), path, players[1 - self][PATH]):
            cullision(turtle)

        print("turning right")         
    def move(self):
        self.forward(self.currentSpeed)
        self.screen.listen()
        wn.onkeypress(self.turnLeft, self.leftTurn)
        wn.onkeypress(self.turnRight, self.rightTurn)
        wn.onkeypress(self.increaseSpeed, self.speedup) 
        wn.onkeypress(self.decreaseSpeed, self.slowdown)    

        
    def increaseSpeed(self):
        self.currentSpeed += 1

    def decreaseSpeed(self):
        self.currentSpeed -= 1

player1 = Player1("a", "d", "w", "s")
player2 = Player2("Left", "Right", "Up", "Down")



while True:
 
    player1.move()
    print(player1.pos()[0])
    player2.move()
    
    #Boundary check for player 1
    #if player1.xcor() > 300 or player1.xcor() < -300:
    if player1.pos()[0] > 300 or player1.pos()[0] < -300:
        print("Game Over")
        quit()
    if player1.pos()[1] > 300 or player1.pos()[1] < -300:
        print ("Game Over")
        quit()

    #Boundary check for player 2
    #if player2.xcor() > 300 or player2.xcor() < - 300:
    if player2.pos()[0] > 300 or player2.pos()[0] < -300:
        print("Game Over")
        quit()
    # if player2.ycor() > 300 or player2.ycor() < -300:
    if player2.pos()[1] > 300 or player2.pos()[1] < -300:
        print("Game Over")
        quit()  
    #Collisions 
    

        check()
    if dead == True:
        break
        quit()
