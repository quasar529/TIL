import random
import imp
import turtle
turtle.shape("turtle")
for i in range(0, 5):
    turtle.forward(100)
    turtle.right(72)
turtle.exitonclick()

for i in range(0, 10):
    turtle.right(36)
    for j in range(0, 5):
        turtle.forward(100)
        turtle.right(72)
turtle.exitonclick()

# 60
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.exitonclick()

# 61
for i in range(0, 3):
    turtle.forward(50)
    turtle.right(120)
turtle.exitonclick()

# 62
for i in range(36):
    turtle.forward(11)
    turtle.right(10)

turtle.exitonclick()

# 63
turtle.color("black", "red")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(150)
turtle.pendown()

turtle.color("black", "yellow")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)
turtle.pendown()

turtle.color("black", "grey")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.penup()
turtle.end_fill()

turtle.exitonclick()

# 64
for i in range(5):
    turtle.forward(100)
    turtle.right(144)
turtle.exitonclick()

# 65

turtle.left(90)
turtle.forward(100)

turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.pendown()

turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)

turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.exitonclick()

# 66
colors = ["red", "brown", "blue", "grey", "green", "purple"]
turtle.pensize(3)
for i in range(8):
    turtle.forward(50)
    turtle.right(45)

    turtle.color(random.choice(colors))

turtle.exitonclick()

# 67

for i in range(10):
    for j in range(8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)

turtle.exitonclick()

# 68

lines = random.randint(5, 10)
for i in range(lines):
    howlong = random.randint(50, 100)
    angle = random.randint(1, 360)
    colors = random.choice(["red", "blue", "grey"])
    turtle.color(colors)

    turtle.forward(howlong)
    turtle.right(angle)

turtle.exitonclick()
