import numpy as np
array=np.array([[50, 60, 70], [67, 88, 90], [60, 78, 97]]) 
print(np.sum(array,axis=1))
print(np.sum(array,axis=0))
print(np.sum(array,axis=1,keepdims=True))

