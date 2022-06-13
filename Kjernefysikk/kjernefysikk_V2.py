import numpy as np

data = np.loadtxt("./Massen_til_nuklider.xps")

class Info:

    """konstanter"""
    u = 1.660539e-27
    c = 2.9972e8

    def __init__(self, m_1_f, m_1_e):

        """regning"""
        self.m_for = 0
        self.m_etter = 0

        self.m_1_f = data[m_1_f, 1]
        self.m_1_e = data[m_1_e, 1]

    def Beregne(self):
        self.dm = self.m_for - self.m_etter

        print('frigjort masse =', self.dm,'u','=',self.dm*Info.u,"kg") 

        """Beregne reaksjonsenergi pr kjernereaksjon fra E=mc^2"""
        self.E = self.dm * Info.u * Info.c**2
        print("Reaksjonsenergi:",self.E,"J")


class one_two(Info):
    def __init__(self, m_1_f, m_1_e, m_2_e):
        super().__init__(m_1_f, m_1_e)
        self.m_2_h = data[m_2_e, 1]

        self.m_for = self.m_1_f
        self.m_etter = self.m_1_e + self.m_2_e

class one_three(Info):
    def __init__(self, m_1_f, m_1_e, m_2_e, m_3_e):
        super().__init__(m_1_f, m_1_e)
        self.m_2_h = data[m_2_e, 1]
        self.m_3_h = data[m_3_e, 1]

        self.m_for = self.m_1_f
        self.m_etter = self.m_1_e + self.m_2_e + self.m_3_e

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