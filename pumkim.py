# %%
import turtle
import random

a = turtle.Turtle()
a.color('pink')
a.fillcolor('black')
a.pencolor('white')
a.speed(0)

t = turtle.Turtle()
t.color('red')
t.fillcolor('white')
t.pencolor('black')
t.speed(0)

b = turtle.Turtle()
b.fillcolor('orange')
b.speed(0)

yAxis = random.randint(-100, -50)
toothColor = (input("What color should the teeth be? "))

# body
def body():
    b.teleport(-1900, 1900)
    b.begin_fill()
    for i in range(4):
        b.forward(3800)
        b.right(90)
    b.end_fill()

# left eye
def lEye():
    a.teleport(-125, 150)
    a.begin_fill()
    a.circle(100)
    a.end_fill()

# right eye
def rEye():
    a.teleport(125, 150)
    a.begin_fill()
    a.circle(100)
    a.end_fill()

# mouth
def mouth():
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
def toothOne():
    t.color(toothColor)
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

def toothTwo():
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


def toothThree():
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

def main():
    body()
    lEye()
    rEye()
    mouth()
    toothOne()
    toothTwo()
    toothThree()

main()

# %%
