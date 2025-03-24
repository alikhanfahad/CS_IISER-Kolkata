import numpy as np
X=np.array([1,2,3,4,5,-30,-99,-21])
print(np.size(X))
def f(x):
         if x<0:
            return 0
         elif x==0:
            return 1
         else:
            return x%3
            
c=np.frompyfunc(f,1,1)
d=c(X)
print(d)
