import numpy as np
a=[]
for x in range(9):
    elements=int(input("Enter nine elements:"))
    a.append(elements)
array=np.array(a)
print(array)
print(array[::-1])
    
