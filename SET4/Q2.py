n=4
#Generate Numpy Arrays for each line
import numpy as np

for x in range(0,n):
    for y in np.arange(1.0,1.0*x+1.5,0.5):
        print(y,end=' ')
    print("\n")


