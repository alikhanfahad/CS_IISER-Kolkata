def f(x):
    return 10**x + x - 4


def bisection_simple(a, b):
    if(f(a)*f(b)>=0):
        print("Invalid interval!")
        return

    #print("Current interval, mid and f-value: [%f, %f]: %f %f" %(a, b, a, f(a)))
    mid = a
   

    
    while (b - a) >= 0.0001:
        
        mid = (a + b)/2.0

        #print("a, f-value, b, f-value, mid, f-value: %f %f %f %f %f" %(a, f(a), b, f(b), mid, f(mid)))
        #print("a = %f f(a) = %f b = %f f(b) = %f mid = %f f(mid) = %f" %(a, f(a), b, f(b), mid, f(mid)))
        print("%f %f %f %f %f %f %f" %(a, f(a), b, f(b), mid, f(mid), b-a))
        if(f(a)*f(mid) < 0):
            b = mid
        else:
            a = mid    

        #print("Current interval, mid and f-value: [%f, %f]: %f %f" %(a, b, mid, f(mid)))

        
    print("Final Accuracy = %f" %(b-a))
    
    return mid





sol = bisection_simple(0.5, 0.6)
print("The root is ", "%.4f"%sol)

# AI Generated

def f(x):
    return 10**x + x - 4

def bisection(a, b, tolerance=0.0001, max_iterations=100):
    """
    Finds a root of f(x) in the interval [a, b] using the bisection method.
    
    Args:
        a (float): Lower bound of the interval.
        b (float): Upper bound of the interval.
        tolerance (float): Desired accuracy for the root (default: 0.0001).
        max_iterations (int): Maximum number of iterations (default: 100).
    
    Returns:
        float: Approximate root of f(x), or None if no root is found.
    """
    if f(a) * f(b) >= 0:
        print("Invalid interval: f(a) and f(b) must have opposite signs.")
        return None

    iteration = 0
    while (b - a) >= tolerance and iteration < max_iterations:
        mid = (a + b) / 2.0
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
        iteration += 1

    if iteration == max_iterations:
        print("Maximum iterations reached without achieving desired accuracy.")
    
    print(f"Final interval: [{a:.6f}, {b:.6f}], accuracy: {b - a:.6f}")
    return (a + b) / 2.0

# Example usage
sol = bisection(0.5, 0.6)
if sol is not None:
    print(f"The root is {sol:.4f}")
