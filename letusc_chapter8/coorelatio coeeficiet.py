import array as arr
import math
a=arr.array('d',[])
b=arr.array('d',[])
n=int(input("enter length of array"))
for i in range(n):
    x=float(input("enter the valueof x"))
    a.append(x)
    y=float(input("enter value of y"))
    b.append(y)
def coorelation(c,d):
    sum_xy=0
    sum_x=0
    sum_y=0
    sum_x2=0
    sum_y2 = 0
    for i in range(n):
        xy=c[i]*d[i]
        sum_xy+=xy
        sum_x+=c[i]
        sum_y+=d[i]
        x2=c[i]*c[i]
        sum_x2+=x2
        y2=d[i] * d[i]
        sum_y2+=y2
    sigmax2=math.pow(sum_x,2)
    sigmay2=math.pow(sum_y,2)
    numerator=(sum_xy-(sum_x*sum_y))
    denominator=math.sqrt(((n*sum_x2)-sigmax2)*((n*sum_y2)-sigmay2))
    r=numerator/denominator
    print("the coorelation coefficient of given data is",r)

coorelation(a,b)

