import numpy as np
a=np.array([[2,4,5,12,22],[6,7,8,34,21],[56,23,78,94,11],[45,65,34,23,24]],int)
print(a.shape)
print(a)
print()
def shifting(b):
    for i in range(4):
            p1=b[i][0]
            p2=b[i][1]
            b[i][0]=b[i][2]
            b[i][1]=b[i][3]
            b[i][2]=b[i][4]
            b[i][3]=p1
            b[i][4]=p2
    print(b)
shifting(a)