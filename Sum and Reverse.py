#sum of digits in number
number=int(input("Enter a value"))
sum=0
while number!=0:
    r=number%10
    sum+=r
    number=int(number/10)
print("the sum of digits in given number:",sum)

#Reverse of a number
org_number=int(input("Enter a value"))
rev_number=0
while org_number>0:
    a=org_number%10
    rev_number=(rev_number*10)+a
    org_number=int(org_number/10)
print("The Reverse of thr given number is :",rev_number)
#sum of first and last
number=input("enter a number")
first_number=number[:1]
lastnumber=number[3:]
total=int(first_number)+int(lastnumber)
print("the sum of first and last digit in number is: ",total)