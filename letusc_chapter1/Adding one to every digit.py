number=int(input("Enter a N digit number"))
add_number=1
count=0
n=number
while n!=0:
    n=n//10
    count=count+1
for i in range(1,count):
    add_number=add_number*10
    add_number=add_number+1
resultant_number=number+add_number
print("the resultant number after adding 1 to every digit is: ",resultant_number)