import numpy as np
import math

def f(x):
    return 10**x + x - 4
    #return math.exp(x) - 5
    #return x*x -5*x + 6

def df(x):
    return math.log(10)*10**x + 1
    #return 2*x - 5
    #return math.exp(x)

def df_num(x):
    h = 0.0001
    return (f(x+h) - f(x))/h

def tabular(low, hi, step):
 i1 = low
 i2 = hi

 l = i1
 r = i2

 f1=f(l)
 l1 = l
	
 l += step
 
 print("%f %f %f" %(low, hi, step))

 for n in np.arange(l, r+step, step):
  f2=f(n)
  print("l1=" + str(l1) + " f(l1)=" + str(f1) + " n=" + str(n) + " f2=" + str(f2)) 
  if f1*f2 < 0.0:
   print(str(l1)+ " " + str(n))
   break
   

  l1 = n
  f1 = f(l1)

 return l1, n


    

def newtonRaphson(x):
    h = f(x)/df(x)
    #h = f(x)/df_num(x)
    
    

    
    
    while abs(f(x)) >= 0.00001:

        h = f(x)/df(x)
        #h = f(x)/df_num(x)
        x = x - h
        
       

        print('x, f, df, h values: %f %f %f %f' %(x, f(x), df(x), h))

       
    print("Final f-value %f" %(f(x)))
    
    return x


l, r = tabular(0, 1, 0.1)
print("The root is ", "%.4f"%newtonRaphson(r))
#print("The root is ", "%.4f"%newtonRaphson(0.6))

# AI Generated

import numpy as np
import math

# Define the function and its analytical derivative
def f(x):
    return 10**x + x - 4

def df(x):
    return math.log(10) * 10**x + 1

# Optional numerical derivative (for flexibility)
def df_num(x, h=0.0001):
    return (f(x + h) - f(x)) / h

def tabular_search(low, high, step):
    """
    Finds an interval [a, b] where f(x) changes sign using a fixed step size.
    
    Args:
        low (float): Lower bound of the search interval.
        high (float): Upper bound of the search interval.
        step (float): Step size for checking function values.
    
    Returns:
        tuple: (a, b) where f(a) * f(b) < 0, or None if no sign change is found.
    """
    current = low
    f_current = f(current)
    
    for next_point in np.arange(low + step, high + step, step):
        if next_point > high:
            break
        f_next = f(next_point)
        if f_current * f_next < 0:
            return current, next_point
        current = next_point
        f_current = f_next
    
    print("No sign change found in the given interval.")
    return None

def newton_raphson(f, df, initial_guess, tolerance=1e-5, max_iterations=100):
    """
    Finds a root of f(x) using the Newton-Raphson method.
    
    Args:
        f (callable): Function to find the root of.
        df (callable): Derivative of the function.
        initial_guess (float): Starting point for iteration.
        tolerance (float): Desired accuracy for the root.
        max_iterations (int): Maximum iterations to prevent infinite loops.
    
    Returns:
        float: Approximate root, or None if no convergence.
    """
    x = initial_guess
    for iteration in range(max_iterations):
        fx = f(x)
        if abs(fx) < tolerance:
            return x
        dfx = df(x)
        if dfx == 0:
            print("Derivative is zero. No solution found.")
            return None
        h = fx / dfx
        x = x - h
        # Optional: Uncomment to debug iterations
        # print(f"Iteration {iteration+1}: x = {x:.6f}, f(x) = {fx:.6f}, h = {h:.6f}")
    
    print("Maximum iterations reached without convergence.")
    return None

# Main execution
low, high, step = 0, 1, 0.1
interval = tabular_search(low, high, step)

if interval:
    a, b = interval
    print(f"Sign change found in interval [{a}, {b}]")
    
    # Use midpoint of the interval as initial guess
    initial_guess = (a + b) / 2
    root = newton_raphson(f, df, initial_guess)
    
    if root is not None:
        print(f"The root is approximately {root:.4f}")
    else:
        print("Newton-Raphson did not converge.")
else:
    print("Could not proceed with Newton-Raphson due to no sign change.")
