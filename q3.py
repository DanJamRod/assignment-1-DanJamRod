"""
draw the drunkard's walk
"""
import random
import turtle
import math

t = turtle.Turtle()

for i in range(100):
    t.seth(0)
    a = random.randint(1,4)
    if a == 1:
        t.lt(180)
        t.fd(20)
    elif a == 2:
        t.lt(270)
        t.fd(20)
    elif a==3:
        t.fd(20)
    else:
        t.lt(90)
        t.fd(20)

turtle.mainloop()