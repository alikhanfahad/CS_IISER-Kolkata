import math
def ff(x):
    ff=math.sin(x)+ x**2 -1
    return ff
a=0.63
b=0.64
accuracy=0.001
while abs(b-a)>accuracy:
    m=(a+b)/2
    print(m)
    if ff(a)*ff(m)<0:
        b=m
    else:
        a=m
        
print(m)
    
