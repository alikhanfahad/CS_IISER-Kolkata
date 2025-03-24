import numpy as np
a=[]
for x in range(9):
    elements=int(input("Enter nine elements:"))
    a.append(elements)
array=np.array(a)

print("Last 3 elements from the array",array[6::])
print("First 3 elements from the array",array[0:3:])
print("Middle 3 elements from the array",array[3:6:1])
print("5th-last element to 2nd-last element(included):",array[-5:-1:-1])
b=array[1::2]
b-=b
print("Updated array:",array)
