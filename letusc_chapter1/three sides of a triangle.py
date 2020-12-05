#Triangle is valid or not
ab=int(input("enter value of side AB"))
bc=int(input("enter value of side BC"))
ca=int(input("enter value of side CA"))

largest=ab
if largest<bc:
    largest=bc
if largest<ca:
    largest=ca
if largest==ab and ab<bc+ca:
    print("The Triangle is Valid")
else:
    print("The Triangle is not Valid")
if largest==bc and bc<ab+ca:
    print("The Traiangle is Valid ")
else:
    print("The Triangle is not Valid")
if largest==ca and ca<ab+bc:
    print("The Triangle is Valid")
else:
    print("The Triangle is not Valid")

#Triangle is Equilateral/Isocelles/Rigth
import math
a=int(input("enter side A of atriangle"))
b=int(input("enter side B of a triangle"))
c=int(input("enter side C of a triangle"))

if a==b==c:
    print("The Triangle is Equilateral Triangle")
if a==b or b==c or c==a:
    print("The triangle is Isocelles Triangle")
largest=a
if largest<b:
    largest=b
if largest<c:
    largest=c
if largest==a and math.pow(largest,2)==math.pow(b,2)+math.pow(c,2):
    print("The Triangle is Rigth Angle Triangle")
if largest==b and math.pow(largest,2)==math.pow(a,2)+math.pow(c,2):
    print("The Triangle is Right Angle Triangle")
if largest==c and math.pow(largest,2)==math.pow(b,2)+math.pow(a,2):
    print("The Triangle is Right Angle Triangle")