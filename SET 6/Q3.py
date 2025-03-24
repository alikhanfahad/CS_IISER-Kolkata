import numpy as np
A=np.array([[1,2,3],[4,8,66],[7,81,9]])
B=np.array([2,3,4])
if abs(np.linalg.det(A)) > 0.00001:
   print(np.linalg.inv(A).dot(B))
