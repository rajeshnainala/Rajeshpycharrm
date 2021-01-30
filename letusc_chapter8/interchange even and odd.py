import numpy as np
a=np.array([2,5,6,7,8,9,4,3])
for i in range(0,len(a),2):
    temp=a[i]
    a[i]=a[i+1]
    a[i+1]=temp
print(a)