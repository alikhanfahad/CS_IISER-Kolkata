a_decimal=int(input("Enter Your Decimal Number:"))

def d2b(x):
    s=""
    quotient=x
    while quotient > 0:
         remainder=quotient%2
         quotient=quotient//2
         s=str(remainder) + s
         #append the remainder to a list
         #invert the list
         #convert the list to string without commas
    return s
b_binary=d2b(a_decimal)
print(b_binary)  
import numpy as np
array=np.array([1,2,3,4,5])
calcbin = np.frompyfunc(d2b, 1, 1)
y = calcbin(array)
print(y)
