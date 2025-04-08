import numpy as np
N=100
x1,h1=np.linspace(0,4,N,endpoint=True,retstep=True)
x2,h2=np.linspace(0,5,N,endpoint=True,retstep=True)
y1=np.sqrt(16-(x1)**2)
y2=np.sqrt((1-((x2)**2/(25)))*36)
rect=(h2*np.sum(y2))-(h1*np.sum(y1))
trap=h2*(0.5*(y2[0]+y2[-1])+np.sum(y2[1:-1])) - h1*(0.5*(y1[0]+y1[-1])+np.sum(y1[1:-1]))
simp=(h2/3)*(y2[0]+y2[-1]+4*np.sum(y2[1:-1:2])+2*np.sum(y2[2:-1:2])) - (h1/3)*(y1[0]+y1[-1]+4*np.sum(y1[1:-1:2])+2*np.sum(y1[2:-1:2]))

from scipy import integrate
trap_scipy=integrate.trapezoid(y=y2,x=x2)- integrate.trapezoid(y=y1,x=x1)
simp_scipy=integrate.simpson(y=y2,x=x2) - integrate.simpson(y=y1,x=x1)

actual=((np.pi*6*5)/4) - ((np.pi*4*4)/4)

p1=(abs(simp_scipy-actual)/actual)*100
print(rect)
print(trap)
print(simp)
print(trap_scipy)
print(simp_scipy)
print(actual)
print(p1)

