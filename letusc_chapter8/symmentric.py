import numpy as np
a=np.array([[3,4],[4,3]],int)
b=a.T
symmentric=0
for i in range(2):
    for j in range(2):
        if a[i][j]==b[i][j]:
            symmentric=1
        else:
            symmentric=0
            break
if symmentric==1:
    print("matrix is symmentric")
else:
    print("matrix is non symmentric")