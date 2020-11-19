#Overtime Pay
for count in range(1,11):
    hours=int(input("enter no of hours worked by person"))
    if hours>40:
        overtime=hours-40
        overtime_pay=overtime *12
        print("the Overtime Pay for the person",count,"is",overtime_pay,"Rupees")
    else:
        print("the person",count,"is not eligible for Overtime Pay")
#factorial of a number
number=int(input("emter a number"))
factorial=1
while number!=0:
    factorial=factorial*number
    number=number-1
print("the factorial of given number is ",factorial)
#power of another number
a=int(input("enter a value of a"))
b=int(input("enter a value of b"))
pow=1
while b!=0:
    pow=pow*a
    b=b-1
print("the power of a to the b is ",pow)
#Ascii values
number=0
while number<=255:
    ascii_value=chr(number)
    print("Ascii value of",number,"is",ascii_value)
    number=number+1