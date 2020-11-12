# who is youngest

ram_age=int(input("Enterthe age of ram"))
shyam_age=int(input("Enter the age of shyam"))
ajay_age=int(input("Enter the age of ajay"))
if ram_age<shyam_age:
     if ram_age<ajay_age:
         print("Ram is youngest among three")
     else:
         print("Ajay is youngest among  three")
else:
    if shyam_age<ajay_age:
        print("Shyam is youngest among three")
    else:
        print("Ajay is youngest among three")
#valid triangle?
angle_a=int(input("enter value of angle A "))
angle_b=int(input("enter value of angle B"))
angle_c=int(input("enter the value of angle C "))
sum=angle_a+angle_b+angle_c
if sum==180:
    print("the given triangle is valid")
else:
    print("the given traingle is not valid")
#Absolute value
integer=int(input("enter a integer number"))
print("the absolute value of integer is:",abs(integer))


# which is greater(area or perimetre)
length=int(input("enter lenth of rectangle"))
breadth=int(input("enter breadth of a triangle"))
area=length*breadth
perimetre=2*(length+breadth)
if area>perimetre:
     print("Area of Rectangle is greater than its Perimetre")
else:
    print("perimetre of a Rectangle is greater than its Area")