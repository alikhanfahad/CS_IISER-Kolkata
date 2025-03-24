d_sum={}
import numpy as np
d={}
for x in range(5):
    a=input("Enter Name")
    k=int(input("Enter Marks in Subject 1"))
    l=int(input("Enter Marks in Subject 2"))
    m=int(input("Enter Marks in Sbject 3"))
    b=np.array([k,l,m])
    b.astype('float64')
    c=np.sum(b)
    d.update({a:c})
print(d)
