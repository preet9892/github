from turtle import  Turtle, Screen
baby = Turtle()
baby.shape("turtle")
baby.color("coral")


def drawTriangle(x):
    x.left(120)
    x.forward(200)
    x.left(120)
    x.forward(200)
    x.left(120)
    x.forward(200)

drawTriangle(baby)
baby.position(-3,-3)
drawTriangle(baby)





newScreen = Screen()
print(newScreen.canvheight)
newScreen.exitonclick()
