import math
def area_of_triangle(a,b,c):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of traingle is",round(area,2),"sq_metres")
area_of_triangle(6,5,4)
