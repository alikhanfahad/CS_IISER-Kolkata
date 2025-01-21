def factorial(n):
    y=1
    for x in range(1,n+1):
        y*=x
    return y
Z=[]
X=[]
for x in range(6):
    for y in range(x+1):
        W= (factorial(x))/(factorial(y)*factorial(x-y))
        Z.append(W)
    X.append(Z)
    Z=[]
for h in range(len(X)):
    for j in range(0,6-h,1):
        print(' ',end=" ")
        l=str(X[h])[1:-1].replace(","," ")
    print(l,end=" ")
    print("\n")

    
 #           1.0 

 #        1.0  1.0 

 #      1.0  2.0  1.0 

 #    1.0  3.0  3.0  1.0 

 #  1.0  4.0  6.0  4.0  1.0 

 # 1.0  5.0  10.0  10.0  5.0  1.0
