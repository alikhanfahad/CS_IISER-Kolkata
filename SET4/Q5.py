L2=[1,2,1,2,2,2,3,4,3,4,5,5,5,6,6]
for x in range(len(L1)):
      if L1[x] in L1 and L1[x] not in L2:
                L2.append(L1[x])


