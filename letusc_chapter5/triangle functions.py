import math
x1=int(input("enter value of x1:"))
y1=int(input("enter value of y1:"))
x2=int(input("enter value of x2:"))
y2=int(input("enter value of y2:"))
x3=int(input("enter value of x3:"))
y3=int(input("enter value of y3:"))
x=int(input("enter valu of x: "))
y=int(input("enter value of y:"))

#To find out hte distance between pionts
def distance_of_points(i1,j1,i2,j2):
    distance=math.sqrt(pow((i2-i1),2)+pow((j2-j1),2))
    return distance

a=distance_of_points(x1,y1,x2,y2)
b=distance_of_points(x2,y2,x3,y3)
c=distance_of_points(x3,y3,x1,y1)

d=distance_of_points(x1,y1,x,y)
e=distance_of_points(x2,y2,x,y)
f=distance_of_points(x3,y3,x,y)


#to find out the area of triangle
def area_of_triangle(k,l,m):
    s = (k + l + m) / 2
    area = math.sqrt(s * (s - k) * (s - l) * (s - m))
    return area

p=area_of_triangle(a,b,c)
q=area_of_triangle(d,e,a)
r=area_of_triangle(e,f,b)
s=area_of_triangle(f,d,c)

def point_lies_in_triangle(g,h,n,o):
    remainder=g-(h+n+o)
    if remainder==0 or remainder<0.1:
        return 1
    else:
        return 0
print(point_lies_in_triangle(p,q,r,s))



