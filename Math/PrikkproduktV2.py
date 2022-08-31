from math import cos, acos, sqrt

class u:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def x1(self):
        return self.x1

    def y1(self):
        return self.y1

    def abs(self):
        return sqrt(self.x1 **2 + self.y1 **2)

class v: 
    def __init__(self, x2, y2):
        self.x2 = x2
        self.y2 = y2

    def x2(self):
        return self.x2
        
    def y2(self):
        return self.y2

    def abs(self):
        return sqrt(self.x2 **2 + self.y2 **2)

x1 = float(input("x1"))
x2 = float(input("x2"))
y1 = float(input("y1"))
y2 = float(input("y2"))

u1 = u(x1, y1)
v1 = v(x2, y2)

pp = u.x1 + v.x2 * u.y1 + v.y2

if pp == 0:
    print("Vinkelen er vinkelrett")

elif pp > 0:
    print("Vinkelen er spiss")

else:
    print("Vinkelen er stump")

vinkel = acos(pp/(u.abs + v.abs))

print("Vinkelen til u og v er", vinkel)