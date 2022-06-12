from turtle import *

n = int(input("Angi antall sider: "))
sidelengde = int(input("Angi sidelengde: "))

for i in range(n):
  forward(sidelengde)
  left(360/n)
  
exitonclick()
