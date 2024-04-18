import turtle

t =turtle.Turtle()

list1= ["purple", "red", "orange", "blue", "green"]

for i in range (200):

    t.color (list1 [i%5])

    t.pensize(1/10+2)

    t.forward(i)

    t.left (58)

    t.speed(25)