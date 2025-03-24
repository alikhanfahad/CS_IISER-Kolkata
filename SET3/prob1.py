import numpy as np
import math
def f(x):
    f=math.sin(x) + x**2 - 1
    return f
#Method of Tabulation With Accuracy
start=0
stop=1
step=start-stop
f1=f(start)
accuracy=0.001
store=0
x=1

while step > accuracy:
    step=step/10
    for x in np.arange(start,stop+step,step):
         f2=f(x)
         if f1*f2<0:  
             break
    store=x
    f1=f(store)
print(store,x) 
         

  
    
    
