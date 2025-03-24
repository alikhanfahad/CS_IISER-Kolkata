import numpy as np
a=np.array([1,2,3,4])
b=np.array([1,2,4,4])

c=[]
for x in range(len(a)):
    if a[x]==b[x]:
       c.append(1)
    else:
       c.append(0)
print(c)
print(all(c))
     
   
