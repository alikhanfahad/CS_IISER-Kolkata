import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
b=np.array([[-1,-2,-3,-4],[-5,-6,-7,-8],[-9,-10,-11,-12],[-13,-14,-15,-16]])
for x in range(0,4,2):
    for y in range(0,4,2):
        a[x][y]=b[x][y]
print(a)

a[::2,::2]=b[::2,::2]
print(a)
