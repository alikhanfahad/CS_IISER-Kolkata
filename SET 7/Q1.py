
import matplotlib.pyplot as plt
import numpy as np

months_var=list(map(int,input("Enter Month Number separated with commas:").split(',')))
months_var=np.array(months_var)
#print(months)
rainfall_var=list(map(int,input("Enter Corresponding Rainfall(mm) separated with commas:").split(',')))
rainfall_var=np.array(rainfall_var)
plt.plot(months_var,rainfall_var,color='r',marker='+',linestyle='none',label='rainfall')
plt.xticks(months_var,labels=[str(months_var[i]) for i in range(len(months_var))])
plt.show()



