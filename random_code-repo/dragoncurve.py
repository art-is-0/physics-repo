# Dragon curve

from turtle import *

class DragonL:
    def __init__(self, angle, sped):
        self.angle = angle
        self.sped = sped

    def Dragon(self):
        seth(self.angle + 90)
        fd(self.sped)

        seth(self.angle)
        fd(self.sped)

        seth(self.angle - 90)
        fd(self.sped)

        seth(self.angle)
        fd(self.sped)

class DragonR:
    def __init__(self, angle, sped):
        self.angle = angle
        self.sped = sped

    def Dragon(self):
        seth(self.angle)
        fd(self.sped)

        seth(self.angle - 90)
        fd(self.sped)

        seth(self.angle)
        fd(self.sped)

        seth(self.angle + 90)
        fd(self.sped)

DrL = DragonL(45, 50)
DrR = DragonR(45 - 90, 50)


while True:
    DrL.Dragon()
    DrR.Dragon()

    DrR = DragonR(45, 50)
    DrL = DragonL(45 - 90, 50)

    DrR.Dragon()
    DrL.Dragon()

    exitonclick()
