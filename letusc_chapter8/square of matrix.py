import numpy as np
import math
a=np.array([[3,4],[4,3]],int)

def squareroot(c):
    sum=0
    for i in range(2):
        for j in range(2):
            k=math.pow(c[i][j],2)
            sum+=k
    squar_root=math.sqrt(sum)
    return round(squar_root,2)
print(squareroot(a))