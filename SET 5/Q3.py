import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(a)
print()

print(a.shape)
print(a.ndim)
print(a[:2,:])
print()
print(a[:2][:])
b=a[1:3,1:3]
c=np.max(b)
for x in range(2):
    for y in range(2):
       b[x][y]=c
print(a)

