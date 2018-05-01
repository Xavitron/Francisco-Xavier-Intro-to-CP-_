from turtle import Turtle, Screen

playGround = Screen()

playGround.screensize(250, 250)
playGround.title("Turtle Keys")

run = Turtle("turtle")
run.speed("fastest")
run.color("blue")
run.penup()
run.setposition(250, 250)

follow = Turtle("turtle")
follow.speed("fastest")
follow.color("red")
follow.penup()
follow.setposition(-250, -250)

def k1():
    run.forward(45)

def k2():
    run.left(45)

def k3():
    run.right(45)

def k4():
    run.backward(45)

def quitThis():
    playGround.bye()

def follow_runner():
    follow.setheading(follow.towards(run))
    follow.forward(8)
    playGround.ontimer(follow_runner, 10)

playGround.onkey(k1, "Up")  # the up arrow key
playGround.onkey(k2, "Left")  # the left arrow key
playGround.onkey(k3, "Right")  # you get it!
playGround.onkey(k4, "Down")

playGround.listen()

follow_runner()

def is_collided_with(self, run):
    return self.rect.colliderect(run.rect)

runner = run(10, 10, 'my_run')
follower = follow(20, 10)
if follow.is_collided_with(run):
    print 'collision!'

 playGround.mainloop()