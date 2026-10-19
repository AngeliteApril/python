# %%
import turtle
import random

a = turtle.Turtle()
t = turtle.Turtle()
t.shape("turtle")
t.setx(random.randint(-200, 200))
t.sety(random.randint(-200, 200))
a.shape("turtle")

for i in range(4):
    a.fd(100)
    a.rt(90)


# %%
