import numpy as np
a=np.array([[2,4,5,12,22],[6,7,8,34,21],[56,23,78,94,11],[45,65,34,23,24],[55,88,66,77,39]],int)
b=np.linalg.det(a)
print(round(b))