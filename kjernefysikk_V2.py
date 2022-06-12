import numpy as np

data = np.loadtxt("./Massen_til_nuklider.xps")

class Info:
    def __init__(self, m_for, m_etter):
        """konstanter"""
        self.u = 1.660539e-27
        self.c = 2.9972e8

        """regning"""
        self.m_for = 0
        self.m_etter = 0

        """Variabler"""
        self.m_for = m_for
        self.m_etter = m_etter

    def Beregne(self):
        self.dm = self.m_for - self.m_etter

        print('frigjort masse =', self.dm,'u','=',self.dm*self.u,"kg") 

        """Beregne reaksjonsenergi pr kjernereaksjon fra E=mc^2"""
        self.E = self.dm * self.u * self.c**2
        print("Reaksjonsenergi:",self.E,"J")

"""""
class Mengde(Info):
    def one_two(self, m_1, m_2, m_3):
        m_1_u = data[m_1, 1]
        m_2_u = data[m_2, 1]
        m_3_u = data[m_3, 1]
        self.m_for = m_1_u
        self.m_etter = m_2_u + m_3_u

    def one_three(self, m_1, m_2, m_3, m_4):
        m_1_u = data[m_1, 1]
        m_2_u = data[m_2, 1]
        m_3_u = data[m_3, 1]
        m_4_u = data[m_4, 1]
        self.m_for = m_1_u
        self.m_etter = m_2_u + m_3_u + m_4_u

"""
print("Hvor mange kjerner er det før?")
metode_for = int(input())

print("Hvor mange kjerner er det etter?")
metode_etter = int(input())

if metode_for == 1:
    print("Hva er nukleon tallet før")
    mf_1 = int(input())
    if metode_etter == 2:
        print("Hva er det første nukleon tallet etter")
        me_1 = int(input())
        print("Hva er det andre nukleon tallet etter")
        me_2 = int(input())
        Oppgave = Info(data[mf_1,2], data[me_1,2] + data[me_2,2])

    if metode_etter == 3:
        print("Hva er det første nukleon tallet etter")
        me_1 = int(input())
        print("Hva er det andre nukleon tallet etter")
        me_2 = int(input())
        print("Hva er det tredje nukleon tallet etter")
        me_3 = int(input())
        Oppgave = Info(data[mf_1,2], data[me_1,2] + data[me_2,2], data[me_3,2])
    Oppgave.Beregne()        

if metode_for == 2:
    print("Hva er nukleon tallet før")
    mf_1 = int(input())
    print("Hva er andre nukleon tallet før")
    mf_2 = int(input())

    if metode_etter == 1:
        print("Hva er det første nukleon tallet før")
        me_1 = int(input())
        print("Hva er det andre nukleon tallet før")
        me_2 = int(input())
        Oppgave = Info(data[mf_1,2] + data[mf_2,2], data[me_1,2])

    if metode_etter == 2:
        print("Hva er det første nukleon tallet før")
        me_1 = int(input())
        print("Hva er det andre nukleon tallet før")
        me_2 = int(input())
        print("Hva er det tredje nukleon tallet før")
        me_3 = int(input())
        Oppgave = Info(data[mf_1,2] + data[mf_2,2], data[me_1,2] + data[me_2,2])

    if metode_etter == 3:
        print("Hva er det første nukleon tallet før")
        me_1 = int(input())
        print("Hva er det andre nukleon tallet før")
        me_2 = int(input())
        print("Hva er det tredje nukleon tallet før")
        me_3 = int(input())
        Oppgave = Info(data[mf_1,2] + data[mf_2,2], data[me_1,2] + data[me_2,2], data[me_3,2])
    Oppgave.Beregne()