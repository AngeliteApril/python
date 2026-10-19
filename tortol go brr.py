# %%
import turtle
import random

a = turtle.Turtle()
t = turtle.Turtle()
t.shape("turtle")
a.penup()
a.setposition(-350, 150)
a.pendown()
t.penup()
t.setposition(-350, -150)
t.pendown()

a.shape("turtle")
a.color("pink")
t.color("red")

while a.xcor() < 350 and t.xcor() < 350:
    a.fd(random.randint(1, 10))
    t.fd(random.randint(1, 10))

if a.xcor() > t.xcor():
    print("a (pink) wins")
if t.xcor() > a.xcor():
    print("t (red) wins")
if a.xcor() == t.xcor():
    print("both think they won. they will fight until nothing is left but themselfs.")


# %%