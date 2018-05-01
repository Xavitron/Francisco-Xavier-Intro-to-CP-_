import turtle 
from turtle import Turtle
import math 
import random 

# mypen = Turtle()
# wn = turtle.Screen()

# #Change background color 
# wn.bgcolor("black")

# #Draw border of the game 
# mypen.penup()
# mypen.speed(10)
# mypen.hideturtle()
# mypen.color("yellow")
# mypen.pensize(3)
# mypen.forward(300)
# mypen.pendown()
# mypen.left(90)
# mypen.forward(300)
# mypen.color("lightgreen")
# mypen.left(90)
# mypen.forward(300)
# mypen.color("yellow")
# mypen.forward(300)
# mypen.color("lightgreen")
# mypen.left(90)
# mypen.forward(300)
# mypen.color("yellow")
# mypen.forward(300)
# mypen.color("lightgreen")
# mypen.left(90)
# mypen.forward(300)
# mypen.color("yellow")
# mypen.forward(300)
# mypen.color("lightgreen")
# mypen.left(90)
# mypen.forward(300)


#I got this from Mr.Cozort week nine code. 

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Python Turtle game with classes... ")
dead = False
class Player(Turtle):

    def __init__(self, left, right, speedup):
        Turtle.__init__(self)
        self.pendown()
        self.speed(0)
        self.shape("arrow")
        self.color("red")
        self.currentSpeed = 1
        self.leftTurn = left
        self.rightTurn = right
        self.speedup = speedup
        #self.slowdown = slowdown
    def turnLeft(self):
        self.left(30)
        print("Turning Left")
    def turnRight(self):
        self.right(30)
        print("Turning Right")
    def move(self):
        self.forward(self.currentSpeed)
        self.backward(self.currentSpeed)
        self.screen.listen()
        wn.onkeypress(self.turnLeft, self.leftTurn)
        wn.onkeypress(self.turnRight, self.rightTurn)
        wn.onkeypress(self.increaseSpeed, self.speedup)
        #wn.onkeypress(self.decreaseSpeed, self.slowdown)

    

    def increaseSpeed(self):
        self.currentSpeed += 1

  #  def decreaseSpeed(self):
   #     self.currentSpeed -= 1 

player1 = Player("a", "d", "w")
player2 = Player("Left", "Right", "Up")


#Set Boundaries

# while True:

#     #Boundary check
#     if player1.xcor() > 300 or player1.xcor() < -300:
#         print("GAME OVER")
#         quit()
    
#     if player1.ycor() > 300 or player1.ycor() < -300:
#         print("GAME OVER")
#         quit()

while True:
    player1.move()
    player2.move()
    if dead:
        break








# # #I got this code from https://codereview.stackexchange.com/questions/149202/catch-the-turtle-python , this is going to help me make a boundarie  
# # #so that the turtles don't go past it.

# # #Draw border
# # mypen = turtle.Turlte()
# # mypen.penup()
# # mypen.speed(10)
# # mypen.hideturtle()
# # mypen.setposition(-300,-300)
# # mypen.pendown()
# # mypen.pensize(3)
# # for side in rage(4):
# #     mypen.color("yellow")
# #     mypen.forward(300)
# #     mypen.color("black")
# #     mypen.forward(300)
# #     mypen.left(90)
# #     mypen.hideturtle()


# # while True:
# #     player1.move()
# #     player2.move()
# #     if dead:
# #         break



# # textTurtle = Turtle()
# # screenText = textTurtle.getscreen()
# # myDialogue = screenText.textimput("Hello there!", "What's your name?")
# # print(myDialogue)
