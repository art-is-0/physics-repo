   # Turtle

import time
from turtle import * 
import random

shape("turtle")
color("purple")


count = 1 
T = 4
n = 3
s = 40

def f(x):
    return 180 - ((x-2)*180/x)
    
while count <= T:
    speed(0)
    forward(s)
    left(f(n))
    count = count + 1
    
    
    if count == T:
        n = n + 1
        T = T + n
        #s = s - 1 #Weird things
    
    
exitonclick()



