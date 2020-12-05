#list of prime numbers
number=1
i=2
prime_list=[]
for number in range(1,301):
    #print(number)
    flag=0
    for i in range(2,(number//2)+1):
        if number%i==0:
            flag=1
            break;
    if flag==0 and number!=1:
        prime_list.append(number)
print(prime_list)

#smile on screen
number=1
smile=chr(number)
for j in range(1,1000):
    print(" ")
    for i in range(1,1000):
         print(smile,end='')
#factorial series
fact=1
sum_fact=0
for i in range(1,8):
    fact=fact*i
    rev_fact=i/fact
    sum_fact=sum_fact+rev_fact
print(sum_fact)

#combinations of 1,2,3
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            if i!=j and i!=k and j!=k:
                print(i,j,k)
#calculation of intelligence
x=0.5
for y in range(1,7):
    while x>=0.5 and x<=12.5:
        i=2*(y+(0.5*x))
        print(i,y,x)
        x=x+0.5
#multiplication table
number=int(input("enter a number for multiplication"))
for i in range(1,number+1):
    m=number*i
    print(number,"*",i,"=",m)
#pricipal Amount
import math
for i in range(1,11):
    p=float(input("enter principal amount"))
    q=float(input("enter interest"))
    r=float(input("enter annual rate"))
    n=float(input("no of years"))
    c=1+(r/q)
    d=n*q
    amount=p*math.pow(c,d)
    print(round(amount,2))

#sum of series
import math
x=int(input("enter value of x"))
term=(x-1)/x
series=0
for i in range(2,8):
    p=math.pow(term,i)
    m=p/2
    series=series+m
series=term+series
print("the sum of series is: ",round(series,3))