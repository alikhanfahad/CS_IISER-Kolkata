L1=[1,2,3,4,5]
L2=[5,4,10,12]
L3=[L1[x]+L2[y] for x in range(len(L1)) for y in range(len(L2)) if L1[x]%2!=0 and L2[y]%2!=0]
print(L3)
