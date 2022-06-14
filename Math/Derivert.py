from pylab import plot, show

while True:
    if input()== "eks":
        x_st = 0
        x_sl = 20
        y_st = 2000
        
        dx = 0.1
        
        k = float(input("What is k?  "))
        
        x = x_st
        y = y_st
        
        while x <= x_sl:
            plot(x,y,'r_')
            x = x + dx
            y = y + k*y *dx
        show()
            
    if input() == "log":
        x_st = 0
        x_sl = 20
        y_st = 1
        
        dx = 0.1
        
        k = float(input("What is k?  "))
        print(k)
        B = float(input("What is B?  "))
        print(B)
        x = x_st
        y = y_st
        
        while x <= x_sl:
            plot(x,y,'b_')
            x = x + dx
            y = y + k*y*(1-y/B) *dx
            print(y)
        show()

    if input()== "normal":
        x_st = 0
        x_sl = 20
        y_st = 2000
        
        dx = 0.1
        
        derivert = float(input("What is derivert?  "))
        
        x = x_st
        y = y_st
        
        while x <= x_sl:
            plot(x,y,'r_')
            x = x + dx
            y = y + derivert *dx
        show()
            