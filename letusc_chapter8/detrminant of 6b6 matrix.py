import numpy as np
a=np.array([[2,4,5,12,22,45],[2,6,7,8,34,21],[3,56,23,78,94,11],[66,45,65,34,23,24],[22,55,88,66,77,39],[67,29,13,65,23,88]],int)
b=np.linalg.det(a)
print(round(b))