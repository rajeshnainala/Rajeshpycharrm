import numpy as np
a=np.array([[2,12,16,1],[6,11,8,3],[56,26,88,22],[45,65,34,23]],int)
print(a)
print()
def sorting(b):
    for i in range(len(b)):
        for j in range(len(b)):
            if j!=len(b)-1:
                if b[i][j]>b[i][j+1]:
                    p1=b[i][j]
                    b[i][j]=b[i][j+1]
                    b[i][j+1]=p1
            else:
                if (i and j)!=len(b)-1:
                    if b[i][j]>b[i+1][0]:
                        p2=b[i][j]
                        b[i][j]=b[i+1][0]
                        b[i+1][0]=p2
                else:
                    break


    print(b)

def sortrowwise(b):
    for i in range(len(b)):
        for j in range(len(b)):
            for k in range(len(b)-j-1):
                if (b[i][k] > b[i][k + 1]):
                    swap= b[i][k]
                    b[i][k] = b[i][k + 1]
                    b[i][k + 1] =swap
    print(b)
sortrowwise(a)
def sortcolumnwise(b):
    for i in range(len(b)):
        for j in range(len(b)):
            for k in range(len(b)-i-1):
                if (b[k][j] > b[k+1][j]):
                    swap= b[k][j]
                    b[k][j] = b[k+1][j]
                    b[k+1][j] =swap
    print(b)
sortcolumnwise(a)
