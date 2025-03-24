from math import sin
def f(x):
    f=sin(x)+ (x**2) -1 
    return f 
    
start=0
stop=1
step=0.001
f1=f(start)
import numpy as np
for y in np.arange(start,stop,step):
     f2=f(y)
     if f1*f2<0:
         print(store,y)
     store=y
     f1=f(store)
    
