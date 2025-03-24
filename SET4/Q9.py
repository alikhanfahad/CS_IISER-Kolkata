import numpy as np
d={}
for x in range(5):
    a=input("Enter Name")
    k=input("Enter Marks in Subject 1")
    l=input("Enter Marks in Subject 2")
    m=input("Enter Marks in Sbject 3")
    b=np.array([k,l,m])
    b.astype('float64')
    d.update({a:b})
print(d)


