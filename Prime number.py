n=int(input("enter the given number "))
count=0

for i in range(1,n):
    if n%i==0:
        count=count+1
if count>=2:
    print("the given number is not prime")
else:
    print("the given number is  prime")





