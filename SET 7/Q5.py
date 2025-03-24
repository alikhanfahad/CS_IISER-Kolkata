
import matplotlib.pyplot as plt
import numpy as np

months_var=list(map(float,input("Enter Month Number separated with commas:").split(',')))
months_var=np.array(months_var)
#print(months)
rainfall_var=list(map(float,input("Enter Corresponding Rainfall(mm) separated with commas:").split(',')))
rainfall_var=np.array(rainfall_var)
temperature_var=list(map(float,input("Enter Corresponding Temperature(celsius) separated with commas:").split(',')))
temperature_var=np.array(temperature_var)

plt.bar(months_var,rainfall_var,color='green',width=0.5)
plt.show()





