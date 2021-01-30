import array as arr
a=arr.array("i",[0])
for i in range(25):
    a[i]=int(input("enter a integer"))
    a.append(a[i])
count=0
exist=0
number=int(input("enter the number to search"))
for i in range(25):
    if a[i]==number:
        exist=1
        count+=1
if exist==1:
    print("the number is found and its count is : ",count)
else:
    print("number is not in array")