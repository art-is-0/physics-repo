import numpy as np

x1, y1, z1 = map(float, input('').split(', '))
vec1 = np.array([x1,y1,z1])

x2, y2, z2 = map(float, input('').split(', '))
vec2 = np.array([x2,y2,z2])

x = np.dot(vec1, vec2)
print('Prikkproduktet er', x)

if x == 0:
    print('Vektorene er ortogonale')

elif x > 0:
    print('Vektoren er stump')

else: 
    print('Vektoren er spiss')

