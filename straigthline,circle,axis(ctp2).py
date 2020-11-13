#Three points in a Straight line
'''x1=int(input("enter value of x1 "))
x2=int(input("enter value of x2 "))
x3=int(input("enter value of x3"))

y1=int(input("enter value of y1 "))
y2=int(input("enter value of y2 "))
y3=int(input("enter value of y3 "))

slope_of_x1y1x2y2=(y2-y1)/(x2-x1)
slope_of_x2y2x3y3=(y3-y2)/(x3-x2)
if slope_of_x1y1x2y2==slope_of_x2y2x3y3:
    print("Three ponts lie in a straight line")
else:
    print("Three points are not in a straight line")

#centre of the circle
import math
circle_x=int(input("enter x coordinate of center point"))
circle_y=int(input("enter y coordinate of center point"))
radius=int(input("enter radius of the circle"))

point_x=int(input("enter x coordinate of point on circle"))
point_y=int(input("enter y coordinate of point on circle"))

distance_pc=math.sqrt(math.pow(point_x-circle_x,2)+math.pow(point_y-circle_y,2))
if distance_pc>radius:
    print("the center is outside of circle")
elif distance_pc<radius:
    print("the center is inside of circle")
else:
    print("the center is present on the circle")'''
#x_axis,y_axis,origin
x4=int(input("enter x coordinate"))
y4=int(input("enter y coordinate"))
if(x4!=0 and y4==0):
    print("point lies on x axis")
elif(x4==0 and y4!=0):
    print("point lies on y axis")
elif(x4==0 and y4==0):
    print("point lies on origin")
else:
    print("point deosnot lies on x and yaxis")