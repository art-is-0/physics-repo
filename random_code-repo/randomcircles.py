from turtle import *
import random
import time

def f(x):
    return 180 - ((x-2)*180/x)

rgb = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray']

while True:
    x = random.randint(-60, 60) 

    if x > 5:
        color(rgb[random.randint(0, len(rgb)-1)])
        begin_fill()

        for _ in range(random.randint(x, x*2)) :
            #color(rgb[random.randint(0, len(rgb)-1)])
            speed(0)
            forward(10)
            right(abs(f(x)))

        end_fill()

    elif x < -5:
        x = abs(x)
        color(rgb[random.randint(0, len(rgb)-1)])
        begin_fill()

        for _ in range(random.randint(x, x*2)) :
            #color(rgb[random.randint(0, len(rgb)-1)])
            speed(0)
            forward(10)
            left(f(x))
        
        end_fill()

    else:
        x = random.randint(-50, 50) 



exitonclick()