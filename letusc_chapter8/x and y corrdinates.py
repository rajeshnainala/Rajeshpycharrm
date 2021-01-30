import array as arr
import math
c=arr.array('d',[])
d=arr.array('d',[])
n=int(input("enter length of array"))
for i in range(n):
    x=float(input("enter the valueof x"))
    c.append(x)
    y=float(input("enter value of y"))
    d.append(y)
def distance_fl(a,b):
    distance=0
    for i in range(n-1):
        d=math.sqrt(pow((a[i+1]-a[i]),2)+pow((b[i+1]-b[i]),2))
        distance+=d
    fl=math.sqrt(pow((a[0]-a[9]),2)+pow((b[0]-b[9]),2))
    distance+=fl
    print("the distance between first and last point is",distance)
distance_fl(c,d)