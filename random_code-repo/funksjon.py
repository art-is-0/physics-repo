from math import log

def f(x):
    return 5*log(x**3 + 2) + x - 6

dx = 0.001

ng = -1.2
øg = 5

x = ng
y = 0

while x < øg:
    if f(x)*f(x+dx) < 0:
        print("Du har et nullpunkt omtrent ved x = ", x)
        
    x = x + dx
    y = y + 1
    
print("Totale runder er",y)
    
