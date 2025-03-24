import math

def f(x):
    #return (1/x)*math.sin(x)
    #return x*math.cos(x)
    return 10**x + x - 4
    #return math.sin(x) + x*x  - 1


import numpy as np

#f = lambda x: 10**x + x - 4

i1 = 0.0 #left interval point
i2 = 1.0 #right interval point

l = i1
r = i2

f1=f(l) #value at 0.0
l1 = l #0.0

step = 0.1

l+=step #0.1

for n in np.arange(l, r+step, step):
    f2=f(n)
    print("l1=" + str(l1) + " f(l1)=" + str(f1) + " n=" + str(n) + " f2=" + str(f2)) 
    if f1*f2 < 0.0:
        print("Desired interval :" + str(l1)+ " " + str(n))
        
        break

       

    l1 = n
    f1 = f(l1)    

    #print(n)

# AI Generated

import numpy as np

def find_root_interval(f, low, hi, accuracy):
    """
    Finds an interval [a, b] where f(x) changes sign, indicating a root.
    
    Args:
        f: Function to evaluate (e.g., lambda x: 10**x + x - 4)
        low: Lower bound of the initial interval
        hi: Upper bound of the initial interval
        accuracy: Desired step size precision
    
    Returns:
        Tuple (a, b) where f(a) * f(b) < 0, or None if no sign change is found
    """
    step = (hi - low) / 10  # Initial step size
    while step >= accuracy:
        # Generate points from low to hi with current step size
        x_values = np.arange(low, hi + step, step)
        for i in range(len(x_values) - 1):
            a = x_values[i]
            b = x_values[i + 1]
            fa = f(a)
            fb = f(b)
            if fa * fb < 0:  # Sign change detected
                return a, b
        step /= 10  # Refine step size for next iteration
    return None  # No sign change found within accuracy

# Example usage
f = lambda x: 10**x + x - 4
interval = find_root_interval(f, 0, 1, 0.01)
if interval:
    print(f"Root found in interval: [{interval[0]}, {interval[1]}]")
else:
    print("No sign change detected within the specified accuracy.")
