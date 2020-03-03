import random

def drunkard_walk(x, y, n):
    """
    x, y: the original location
    n: the number of intersections(steps)

    return the Manhattan distance after n intersections(steps) from the origin
    """
    x_0 = x # Starting coordinatesn defined as x_0 and y_0 so not forgotten
    y_0 = y
    for i in range(n): # The program repeats "n" times to simulate the drunkard taking "n" steps 
        a = random.randint(1,4) # 4 possible directions, N, S, E, W -> Chooses one at random
        if a == 1: # 1 in 4 chance
            x += -1 # Simulate a step West
        elif a == 2: # 1 in 4 chance
            y += -1 # Simulate a step South
        elif a==3: # 1 in 4 chance
            x += 1 # Simulate a East
        else: # 1 in 4 chance
            y += 1 # Simulate a step North
    return abs(x_0 - x) + abs(y_0 - y) # Returns blocks North or South added to blocks East or West (manhattan distance)       


def main():
    x_0 = 3 # Simulate starting at x = 3
    y_0 = -5 # Simulate starting at y = -5
    steps = 100 # Simulate 100 steps
    print(f"The drunkard started from ({x_0}, {y_0}).")
    distance = drunkard_walk(x_0, y_0, steps)
    print(f"After {steps} intersections, he's {distance} blocks from where he started.")


if __name__ == '__main__':
    main()