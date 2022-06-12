from math import pi
import numpy as np

data = np.loadtxt("./StrålingsbalansePlaneter.txt", delimiter=", ")


class Info:
    def __init__(self, albedo, distance, radius):
        self.albedo =  albedo
        self.distance = distance
        self.radius = radius
        self.sigma = 5.67E-8        # Stefan-Boltzmanns kontant
        self.r_sol = 6.95E8         # m solas radius
        self.T_sol = 5800           # K Solas overflatetemperatur i Kelvin

    def Regning(self):
        self.A_sol = 4*pi*self.r_sol**2

        self.P_sol = self.sigma*self.T_sol**4*self.A_sol #Stefan-Boltzmanns lov 
        print("Utstrålt effekt fra sola:", self.P_sol, "W")
    
        self.I_s = self.P_sol/(4*pi*self.distance**2)   # innstrålt effekt pr m^2 på jorda
        print("Innstrålt effekten er", self.I_s,"W/m^2")

        self.Overflate = (4*pi*self.radius**2)   # Halvparten av venus overflate m^2
        self.P_inn = self.I_s * pi*self.radius**2 *(1- self.sigma)   # Innstrålt effekt på venus

        print(f"Den total innstrålte effekten er {self.P_inn}W")

        # Gjennomsnittlig overflate temperatur på jorda
        # P_inn = P_ut
        self.Temperatur = (self.P_inn/(self.sigma*self.Overflate))**(1/4)
        print(f"Temperaturen: {self.Temperatur-273} C")

print("Er objektet en planet (1) eller noe annet (2)")
metode = int(input())

if metode == 1:
    print("Hvilken planet? Merkur (0), Venus (1), Jorden (2), Mars (3), Jupiter (4), Saturn (5), Uranus (6), Neptun (7)")
    x = int(input())
    data = np.loadtxt(r"./StrålingsbalansePlaneter.txt", delimiter=", ")
    Oppgave = Info(data[x,0], data[x,1], data[x,2])
    Oppgave.Regning()

if metode == 2:
    print("Hva er albedo?")
    x = float(input())
    print("Hva er distansen?")
    y = float(input())
    print("Hva er radius?")
    z = float(input())

    Oppgave = Info(x,y,z)
    Oppgave.Regning()