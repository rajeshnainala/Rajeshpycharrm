import array as arr
a=arr.array("i",[0])
for i in range(25):
    a[i]=int(input("enter a integer"))
    a.append(i)
a.pop()
def postive_negative(b):
    positive=0
    negative=0
    for i in range(25):
        if b[i]>=0:
            positive+=1
        else:
            negative+=1
    print("number of positive numbers is: ",positive)
    print("number of negative numbers is: ",negative)
def odd_even(c):
    even=0
    odd=0
    for i in range(25):
        if c[i]%2==0:
            even+=1
        else:
            odd+=1
    print("number of even numbers is: ",even)
    print("number of odd numbers is: ",odd)
odd_even(a)
postive_negative(a)