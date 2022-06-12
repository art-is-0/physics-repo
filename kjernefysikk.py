
"""konstanter"""
u = 1.660539e-27 #atommasseenheten
c = 2.99792e8 #lyshastigheten i vakum

"""massen til kjente nuklider i u"""
m_p = 1.00727646688 #massen til protonet i u
m_e = 0.000548579909 #massen til elektronet
m_n = 1.00866 #massen til nøytronet
m_H1 = 1.0078250321 #massen til hydrogen-1
m_H2 = 2.01410
m_H3 = 3.01603
m_He3 = 3.01605
m_He4 = 4.00260
m_Be8 = 8.00530510
m_C12 = 12
m_U235 = 235.04392 
m_Sr88 = 87.905614
m_Xe136 = 135.907219

"""Beregne frigjort masse"""

m_for = m_H2 + m_H2 #massen før reaksjon i antall u
m_etter = m_He4 #massen etter reaksjon i antall u

dm = m_for - m_etter #frigjort masse i antall u

print('frigjort masse =', dm,'u','=',dm*u,"kg") 

"""Beregne reaksjonsenergi pr kjernereaksjon fra E=mc^2"""
E = dm * u * c**2
print("Reaksjonsenergi:",E,"J")
