import turtle
from turtle import *

turtle.home()
turtle.begin_poly()
turtle.fd(100)
turtle.left(20)
turtle.fd(30)
turtle.left(60)
turtle.fd(50)
turtle.end_poly()
p = turtle.get_poly()
register_shape("myFavouriteShape", p)
shape("myFavouriteShape")
done()