def f(x):
    return 10**x + x - 4



import numpy as np

def tabular(low, hi, accuracy):
    x = []
    y = []
    step = hi - low
    while step != accuracy:
        step = step/10.0
        i1 = low
        i2 = hi

        l = i1
        r = i2

        f1=f(l)
        l1 = l

        

        l+=step

        for n in np.arange(l, r+step, step):
            f2=f(n)
            print("l1=" + str(l1) + " f(l1)=" + str(f1) + " n=" + str(n) + " f2=" + str(f2))
            x.append(l1)
            y.append(n) 
            if f1*f2 < 0.0:
                print("Found in: " + str(l1)+ " " + str(n))
                
                break
            
              

            l1 = n
            f1 = f(l1)
            
    return l1, n, x, y


l, r, x, y = tabular(0, 1, 0.1)

print("The final interval: (%f, %f)" %(l, r))


#AI Generated

def find_sign_change_interval(f, low, high, step):
    """
    Finds an interval [a, b] where f(x) changes sign using a fixed step size.
    
    Args:
        f: Function to evaluate
        low: Lower bound of the interval
        high: Upper bound of the interval
        step: Step size for checking the function values
    
    Returns:
        Tuple (a, b) where f(a) * f(b) < 0, or None if no sign change is found
    """
    current_point = low
    current_value = f(current_point)
    
    for next_point in [low + i * step for i in range(1, int((high - low) / step) + 1)]:
        if next_point > high:
            break
        next_value = f(next_point)
        if current_value * next_value < 0:
            return (current_point, next_point)
        current_point = next_point
        current_value = next_value
    
    return None

# Example usage
def f(x):
    return 10**x + x - 4

interval = find_sign_change_interval(f, 0.0, 1.0, 0.1)
if interval:
    print(f"Found interval where f(x) changes sign: [{interval[0]}, {interval[1]}]")
else:
    print("No sign change found in the given interval.")
