import numpy as np
N=10
x,h=np.linspace(1,2,N,endpoint=True,retstep=True)
y=1/x
print(h*np.sum(y))
print(h*(0.5*(y[0]+y[-1])+np.sum(y[1:-1])))
print((h/3)*(y[0]+y[-1]+4*np.sum(y[1:-1:2])+2*np.sum(y[2:-1:2])))
from scipy import integrate
print(integrate.trapezoid(y=y,x=x))
print(integrate.simpson(y=y,x=x))

