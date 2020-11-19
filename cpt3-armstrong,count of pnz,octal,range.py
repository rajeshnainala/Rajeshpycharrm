#Armstrong number from 1 to 500
import math
number=1
for number in range(1,501):
    n=number
    r=0
    cube=0
    sum=0
    while n>0:
        r=n%10
        cube=math.pow(r,3)
        sum=sum+cube
        n=n//10
    if sum==number:
       print(number)
#count of positive, negative,zero
wanted_numbers=int(input("enter how many numbers needed: "))
list=[]
count_positive=0
count_negative=0
count_zero=0
for i in range(wanted_numbers):
    number=int(input("enter value"))
    list.append(number)
for j in list:
    if j>0:
        count_positive+=1
    elif j<0:
        count_negative+=1
    else:
        count_zero+=1
print("No of positive numbers in list is: ",count_positive)
print("No of negative numbers in list is: ",count_negative)
print("No of Zeros in list: ",count_zero)

#octal number
number=int(input("enter a value"))
octal_number=0
r=0
n=number
while n!=0:
    r=(r*10)+ n%8
    if r==0:
        count=1
    n=n//8
while r!=0:
    octal_number=(octal_number*10)+r%10
    r=r//10
if count==1:
    octal_number=octal_number*10
print("the octalnumber of a",number,"is",octal_number)

#range of numbers
numbers=[35,67,9,18,99,16,22]
max=numbers[0]
min=numbers[0]
for i in range(0,len(numbers)):
    if numbers[i]>max:
        max=numbers[i]
    elif numbers[i]<min:
        min=numbers[i]
range=max+min
print("the range of the numbers in a given list is: ",range)





