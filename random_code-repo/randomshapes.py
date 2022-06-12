from turtle import *
import random
import time

shape("turtle")


def f(x):
    return 180 - ((x-2)*180/x)

rgb = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray']

while True:
    x = random.randint(-9,9) 

    if x >= 3:
        #pencolor((random(0,255), random(0,255), random(0,255)))
        color(rgb[random.randint(0, len(rgb)-1)])
        sped = random.randint(30, 75)

        begin_fill()

        for _ in range(random.randint(x, x*2)) :
            #color(rgb[random.randint(0, len(rgb)-1)])
            speed(0)
            forward(sped)
            right(abs(f(x)))

        end_fill()

    elif x <= -3:
        x = abs(x)
        color(rgb[random.randint(0, len(rgb)-1)])
        sped = random.randint(30, 75)

        begin_fill()

        for _ in range(random.randint(x, x*2)) :
            #color(rgb[random.randint(0, len(rgb)-1)])
            speed(0)
            forward(sped)
            left(f(x))
        
        end_fill()

    elif x == -9:
        x = 100
        color(rgb[random.randint(0, len(rgb)-1)])
        sped = random.randint(30, 75)

        begin_fill()

        for _ in range(random.randint(x, x*2)) :
            #color(rgb[random.randint(0, len(rgb)-1)])
            speed(0)
            forward(sped/13)
            left(f(x))
        
        end_fill()

    elif x == 9:
        x = 100
        color(rgb[random.randint(0, len(rgb)-1)])
        sped = random.randint(30, 75)

        begin_fill()

        for _ in range(random.randint(x, x*2)) :
            #color(rgb[random.randint(0, len(rgb)-1)])
            speed(0)
            forward(sped/13)
            right(f(x))
        
        end_fill()

    else:
        x = random.randint(-9, 9) 

exitonclick()