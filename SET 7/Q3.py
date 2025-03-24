
import matplotlib.pyplot as plt
import numpy as np

months_var=list(map(int,input("Enter Month Number separated with commas:").split(',')))
months_var=np.array(months_var)
#print(months)
rainfall_var=list(map(int,input("Enter Corresponding Rainfall(mm) separated with commas:").split(',')))
rainfall_var=np.array(rainfall_var)
temperature_var=list(map(int,input("Enter Corresponding Temperature(celsius) separated with commas:").split(',')))
temperature_var=np.array(temperature_var)
plt.plot(months_var,rainfall_var,color='r',marker='+',linestyle='none',label='rainfall')
plt.plot(months_var,temperature_var,color='g',marker='*',markersize=8,linestyle=’none’label='temperature')
plt.xlabel('months')
plt.legend()
plt.title('Month vs Rainfall vs Temperature Plot')
plt.show()



