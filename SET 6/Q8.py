import numpy as np
L=[1,2,3,4,5,6,7,8,9]
Lout=[]
def f(x):
    return x**3 + 1
for y in range(len(L)):
    b=f(L[y])
    Lout.append(b)
print(Lout)

array=np.array(L)
c=np.frompyfunc(f,1,1)
d=c(array)
print(d)


