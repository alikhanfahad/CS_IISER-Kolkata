def f(x):
  f= x**3 + x**2 -x
  return f
def df(x):
    df=3*x**2 + 2*x -1
    return df
x=1
accuracy=0.0001
while f(x)>accuracy:
     x=x-(f(x)/df(x))
print(x)
