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