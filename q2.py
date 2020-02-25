import random

def drunkard_walk(x, y, n):
    """
    x, y: the original location
    n: the number of intersections(steps)

    return the Manhattan distance after n intersections(steps) from the origin
    """
    for i in range(n):
        a = random.randint(1,4)
        if a == 1:
            x += -1
        elif a == 2:
            y += -1
        elif a==3:
            x += 1 
        else:
            y += 1
    return abs(x) + abs(y)           


def main():
    x_0 = 0
    y_0 = 0
    steps = 100
    print(f"The drunkard started from ({x_0}, {y_0}).")
    distance = drunkard_walk(x_0, y_0, steps)
    print(f"After {steps} intersections, he's {distance} blocks from where he started.")


if __name__ == '__main__':
    main()