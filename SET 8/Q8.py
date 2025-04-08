#use np.random.normal
#given each number here run the logic for assigning the number of times the six words occured
#once you have thatt use the pie plot for showing the results

#np.random.seed(42)
#np.random.normal(size = 1000, loc = 50, scale = 100)

import numpy as np
import matplotlib.pyplot as plt
occurences=np.random.normal(11,4,1000)

bullseye=0
pro=0
seasoned=0
improver=0
beginner=0
miss=0
for x in range(len(occurences)):
    if occurences[x]<=1:
        bullseye+=1
    elif occurences[x]<=4 and occurences[x]>1:
        pro+=1
    elif occurences[x]<=6 and occurences[x]>4:
        seasoned+=1
    elif occurences[x]<=8 and occurences[x]>6:
        improver+=1
    elif occurences[x]<=10 and occurences[x]>8:
        beginner+=1
    else:
        miss+=1
y=[]
y.append(bullseye)
y.append(pro)
y.append(seasoned)
y.append(improver)
y.append(beginner)
y.append(miss)
y=np.array(y)
x=np.array(["Bull's Eye","Pro","Seasoned","Improver","Beginner","Miss"])
plt.pie(y,labels=x)
plt.show()
        

