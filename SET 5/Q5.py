import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
b=np.array([a[:2,:2],a[2:,:2],a[2:,:2],a[2:,2:]])
print(b,b.ndim,b.shape)


