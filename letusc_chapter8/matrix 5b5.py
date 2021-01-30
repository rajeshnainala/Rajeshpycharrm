import numpy as np
a=np.array([[2,4,5,12,22],[6,7,8,34,21],[56,23,78,94,11],[45,65,34,23,24],[55,88,66,77,39]],int)
print(a.shape)
largest=a[0][0]
for i in range(5):
    for j in range(5):
        if a[i][j]>largest:
            largest=a[i][j]
print(largest)