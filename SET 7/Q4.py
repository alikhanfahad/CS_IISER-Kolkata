
import matplotlib.pyplot as plt
import numpy as np

months_var=list(map(float,input("Enter Month Number separated with commas:").split(',')))
months_var=np.array(months_var)
#print(months)
rainfall_var=list(map(float,input("Enter Corresponding Rainfall(mm) separated with commas:").split(',')))
rainfall_var=np.array(rainfall_var)
temperature_var=list(map(float,input("Enter Corresponding Temperature(celsius) separated with commas:").split(',')))
temperature_var=np.array(temperature_var)


plt.subplot(1,2,1)
plt.plot(months_var,rainfall_var,color='r',marker='+',linestyle='none',label='rainfall')
plt.xlabel('Months')
plt.ylabel('Rainfall')
plt.title('Months vs Rainfall')
plt.subplot(1,2,2)
plt.plot(months_var,temperature_var,color='g',marker='*',linestyle='none',label='temperature')
plt.xlabel('Months')
plt.ylabel('Temperature')
plt.title('Months vs Temperature')
plt.show()

plt.subplot(2,1,1)
plt.plot(months_var,rainfall_var,color='r',marker='+',linestyle='none',label='rainfall')
plt.xlabel('Months')
plt.ylabel('Rainfall')
plt.title('Months vs Rainfall')
plt.subplot(2,1,2)
plt.plot(months_var,temperature_var,color='g',marker='*',linestyle='none',label='temperature')
plt.xlabel('Months')
plt.ylabel('Temperature')
plt.show()
plt.title('Months vs Temperature')
