#Fahad
def f(x):
    f=10**x + x -4
    return f
from math import sin
def ff(x):
    f=sin(x)+(x**2)-1
    return f

start=0
stop=1
step=0.1
f1=f(start)
import numpy as np
for y in np.arange(start+step,stop+step,step):
    f2=f(y)
    if f2*f1<0:
        break
    store=y
    f1=f(store)
print(store,y)
#start,stop,step,f1,f2,y,store
    
    
