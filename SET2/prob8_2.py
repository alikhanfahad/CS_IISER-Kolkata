for i in range(0,5):
    for j in range(0,i+1,1):
        print(' ',end=" ")
    for k in range(i+1,6,1):
        print(str(k),end=" ")
    for l in range(4,i,-1):
        print(str(l),end=" ")
    print("\n")
