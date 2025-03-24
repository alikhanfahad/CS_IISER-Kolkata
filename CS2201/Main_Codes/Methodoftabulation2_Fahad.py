#Fahad
import numpy as np
import math
def f(x):
    f=10**x + x - 4
    return f
def ff(x):
    ff=math.sin(x)+ x**2 -1
    return ff
start=0
stop=1
accuracy=0.1
step=stop-start
f1=ff(start)

while abs(step)>accuracy:
    step=step/10
    for x in np.arange(start+step,stop+step,step):
        f2=ff(x)
        if f1*f2<0:
            break
        store=x
        f1=ff(store)
print(store,x)
