import numpy as np
import math
def f(x):
    f=math.sin(x) + x**2 - 1
    return f
    
#Bisection
b=0
a=1
accuracy=0.001
while abs(b-a)>accuracy:
    c=(a+b)/2
    if f(a)*f(c)<0:
        b=c
    else:
        a=c
print(c)
