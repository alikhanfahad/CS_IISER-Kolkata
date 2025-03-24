import matplotlib.pyplot as plt
import numpy as np

months_var=list(map(float,input("Enter Month Number separated with commas:").split(',')))
months_var=np.array(months_var)
#print(months)
rainfall_var=list(map(float,input("Enter Corresponding Rainfall(mm) separated with commas:").split(',')))
rainfall_var=np.array(rainfall_var)
temperature_var=list(map(float,input("Enter Corresponding Temperature(celsius) separated with commas:").split(',')))
temperature_var=np.array(temperature_var)

plt.pie(rainfall_var,labels=months_var)
plt.show()



