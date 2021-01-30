import array as arr
import math
c=arr.array('d',[])
d=arr.array('d',[])
sum_x=0
sum_y=0
sum_xy=0
sum_x2=0
n=int(input("enter length of array"))
for i in range(n):
    x=float(input("enter the valueof x"))
    c.append(x)
    y=float(input("enter value of y"))
    d.append(y)
    sum_x+=c[i]
    sum_y+=d[i]
    xy=c[i]*d[i]
    sum_xy+=xy
    x2=c[i]*d[i]
    sum_x2+=x2
mean_y=sum_y/n
mean_x=sum_x/n
b=((n*sum_xy)-(sum_x*sum_y))/((n*sum_x2)-(math.pow(sum_x,2)))
a=mean_y-(b*mean_x)
for i in range(n):
    print(c[i],"=",a,"+",b*d[i])


