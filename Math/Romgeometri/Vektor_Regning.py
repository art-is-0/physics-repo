import numpy as np

class vector_calculation:
    
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.v1 = np.array([x1,y1,z1])
        self.v2 = np.array([x2,y2,z2])

    def prikkprodukt(self):
        prikk = np.dot(self.v1, self.v2)
        
        if prikk == 0:
            print('Vektorene er ortogonale')

        elif prikk > 0:
            print('Vektoren er stump')

        else: 
            print('Vektoren er spiss')
            
        print('Prikkproduktet er', prikk)

        return prikk
    
    def kryssprodukt(self):
        x = np.cross(self.v1, self.v2)
        #  = np.cross(self.v1, self.v2)
        # print(kryss)

        # if kryss == 0:
        #     print('Vektorene er pararelle')

        return x
    

x=vector_calculation(2,5,6,2,3,5)
x.prikkprodukt()