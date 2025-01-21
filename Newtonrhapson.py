def f(x):
    f=x**3 +x**2 - x
    return f
x=1
def df(x):
    df=3*x**2 +2*x -1
    return df
while f(x)>0.000001:
    x=x-(f(x)/df(x))
print(x)    
