import numpy as np
X=np.array([1,2,3,4,5,-30,-99,-21])
def f(X):
    for y in range(np.size(X)):
         if X[y]<0:
            print(0)
         elif X[y]==0:
            print(1)
         else:
            print(X[y]%3)
       
f(X)

