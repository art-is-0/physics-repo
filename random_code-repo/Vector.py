import sys
from pylab import *

x = []
y = []


while True:
    ob = input("Point or Vector or Plot? ")
    print(ob)
    if "vector" in ob:
        for i in range(0,2):
            x_1 = input("X-value of the vector? ")
            x.append(x_1)
            y_1 = input("Y-value of the vector? ")
            y.append(y_1)
        figure(1)
        plot(x,y,'b-')
        title('Vectors')
        x.clear()
        y.clear()
        
    elif "point" in ob:
        x_1 = input("X-value of the vector? ")
        x.append(x_1)
        y_1 = input("Y-value of the vector? ")
        y.append(y_1)
        
        figure(1)
        X = plot([x])
        Y = plot([y])
        title('Vectors')
        x.clear()
        y.clear()
        
        scatter(X,Y)
        
        
        
    else:
        sys.exit("Here is the plot")
        