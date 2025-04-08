import numpy as np
N=10
x,h=np.linspace(0,5,N,endpoint=True,retstep=True)
y=np.sqrt(25-(x)**2)
rect=h*np.sum(y)
trap=h*(0.5*(y[0]+y[-1])+np.sum(y[1:-1]))
simp=(h/3)*(y[0]+y[-1]+4*np.sum(y[1:-1:2])+2*np.sum(y[2:-1:2]))
import scipy as scipy
trap_scipy=scipy.integrate.trapezoid(y=y,x=x)
trap_scipy=scipy.integrate.simpson(y=y,x=x)
actual=(np.pi*5*5)/4

p1=(abs(rect-actual)/actual)*100
print(p1)

