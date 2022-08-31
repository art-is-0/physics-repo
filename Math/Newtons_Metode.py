#Newtons Metode

class Regning:

    dx = 0.0001

    def f(x):
        return x**2+x+12
    
    def deri(x):
        return (Regning.f(x)-Regning.f(x-Regning.dx))/Regning.dx
        
    def __init__(self, x1):
        self.x1 = x1

    def utregning(self):
        while abs(Regning.f(self.x1)) > 0.01:
            print(self.x1)
            self.x2 = self.x1 - Regning.f(self.x1)/Regning.deri(self.x1)
            self.x1 = self.x2

print("Which next x-value u want to find")
x = float(input())

Gjør = Regning(x)
Gjør.utregning()
