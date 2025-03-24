import matplotlib.pyplot as plt
import numpy as np

import random as rd
n=int(input("Enter the number of simulations needed:"))
num_var=np.arange(1,n+1,1)
prob_var=[]
i=0
heads=0
for x in range(n):
    i+=1
    if rd.random()>0.5:
       heads+=1
    else:
        heads=heads
    prob_head=heads/i
    prob_var.append(prob_head)

prob_var=np.array(prob_var)
plt.plot(num_var,prob_var)
plt.xlabel('Trial Number')
plt.ylabel('Probability of getting head')
plt.title('Probability of Head in a Coin Toss')
plt.show()
