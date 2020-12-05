import math
length=float(input("Enter the lenth of rectangle in meters"))
breath=float(input("Enter the breath of rectangle in meters"))
radius=float(input("Enter the raddius of the circle in meters"))
reactangle_area=length*breath
perimetre=2*(length+breath)
circle_area=2*math.pi*radius*radius
circumference=2*math.pi*radius
print("Area of the Recatangle:",round(reactangle_area,2),"sqmts")
print("Perimetereof the rectangle:",round(perimetre,2),"mts")
print("Area of the circle: ",round(circle_area,2),"sqmts")
print("Circumference  of the Circle: ",round(circumference,2),"mts")