import numpy as np
import random as random
import matplotlib.pyplot as plt
outcome=0
trialsoutcome=[]
trialnumber=[]

trialoutcome_alphabet=['one','two','three','four','five','six']
trialoutcome_number=[1,2,3,4,5,6]
i=0
while outcome!=6:
    num=random.uniform(0,7)
    if num<1:
        #outcome='one'
        outcome=1
    elif num>=1 and num<2:
        #outcome='two'
        outcome=2
    elif num>=2 and num<3:
        #outcome='three'
        outcome=3
    elif num>=4 and num<5:
        #outcome='four'
        outcome=4
    elif num>=5 and num<6:
        #outcome='five'
        outcome=5
    else:
        #outcome='six'
        outcome=6
    trialsoutcome.append(outcome)
    i+=1
    trialnumber.append(i)
    
trialsoutcome=np.array(trialsoutcome)
print(trialsoutcome)
trialnumber=np.array(trialnumber)
print(trialnumber)

#for x in range(trialsoutcome):
 #   if trialsoutcome[x]==1:
        

plt.plot(trialnumber,trialsoutcome,color='r',marker='+',linestyle='-')
plt.xticks(trialnumber,labels=[str(trialnumber[i]) for i in range(len(trialnumber))])
plt.yticks(trialoutcome_number,labels=[str(trialoutcome_alphabet[i]) for i in range(len(trialoutcome_alphabet))])
plt.xlabel("Trial Number")
plt.ylabel("Trial Outcomes(from 1-6)")

 #“start” and “stop” respectively on the plot using matplotlib.pyplot.text(x, y, t) [prints t on the plot at (x,y)].
plt.text(trialnumber[0],trialsoutcome[0],"start")
plt.text(trialnumber[-1],trialsoutcome[-1],"stop")
plt.show()

