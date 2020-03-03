"""
draw the drunkard's walk
"""
import random
import turtle
import math

t = turtle.Turtle() # Create a turtle

for i in range(100): # Range 100 to simulate 100 steps
    t.seth(0) # Sets Turtle initially pointing East for every step -> This is so the result will be consistent with Q2 if using a random.seed()
    a = random.randint(1,4) # Same as Q2: 4 possible directions, N, S, E, W -> Chooses one at random
    if a == 1: # From Q2, a = 1 simulates a step West
        t.lt(180) # Turns 180° left so turtle is pointing West
        t.fd(20) # Move the turtle forwards 20 pixels
    elif a == 2: # From Q2, a = 2 simulates a step South
        t.lt(270) # Turns 270° left so turtle is pointing South
        t.fd(20) # Move the turtle forwards 20 pixels
    elif a==3: # From Q2, a = 3 simulates a step East
        t.fd(20) # Move the turtle forwards 20 pixels (no need to change direction as already pointing East)
    else: # From Q2, a != 1,2,3 simulates a step North
        t.lt(90) # Turns 90° left so turtle is pointing North
        t.fd(20) # Move the turtle forwards 20 pixels

turtle.mainloop()