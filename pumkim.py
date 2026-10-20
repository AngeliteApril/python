# %%
import turtle
import random

a = turtle.Turtle()
a.color("pink")
a.fillcolor('orange')
a.pencolor('black')
a.speed(0)

t = turtle.Turtle()
t.color("red")
t.fillcolor('white')
t.pencolor('black')
t.speed(0)

# body
a.speed(0)
a.teleport(-1900, 1900)
a.begin_fill()
for i in range(4):
    a.forward(3800)
    a.right(90)
a.end_fill()

#reset
a.fillcolor('black')
a.pencolor('white')
a.speed(0)

# left eye
a.teleport(-125, 150)
a.begin_fill()
a.circle(100)
a.end_fill()

# right eye
a.teleport(125, 150)
a.begin_fill()
a.circle(100)
a.end_fill()

# mouth
yAxis = random.randint(-100, -50)

a.teleport(0, yAxis)
a.begin_fill()
a.forward(325)
a.right(90)
a.forward(125)
a.right(90)
a.forward(650)
a.right(90)
a.forward(125)
a.right(90)
a.forward(325)
a.end_fill()

# teeth
for i in range(1):
    t.teleport(random.randint(125, 250), yAxis)
    t.begin_fill()
    t.forward(50)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(75)
    t.right(180)
    t.end_fill()

for i in range(1):
    t.teleport(random.randint(-250, -125), yAxis)
    t.begin_fill()
    t.forward(50)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(75)
    t.right(180)
    t.end_fill()


t.teleport(random.randint(-124, 100), (yAxis - 125))
t.begin_fill()
t.right(90)
t.forward(50)
t.right(90)
t.forward(75)
t.right(90)
t.forward(50)
t.right(90)
t.forward(75)
t.end_fill()


# %%
