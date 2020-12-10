#prime numbers from 1 to 300
number=1
i=2
prime_list=[]
for number in range(1,301):
    #print(number)
    flag=0
    for i in range(2,(number//2)+1):
        if number%i==0:
            flag=1
            break
    if flag==0 and number!=1:
        prime_list.append(number)
print(prime_list)
#using break and continue on same list
list=[3,5,8,9,10,11,13,15]
for i in list:
    if i==9:
        print(i)
        break;# breaks the statement when i = 9
list1=[3,5,8,9,10,11,13,15]
for i in list1:
    if i==9:
        continue # continue in the loop and leaves 9 and print the remaining values in list
    else:
        print(i,end=' ')
#using continue
list3=['python','java','c_sharp','django','html','sql']
for i in list3:
    if i=='python' or i=='django':
        continue
    else:
        print(i)
#using break to know no of values required get sum 24
sum=0
i=1
count=0
for i in range(1,10):
    sum=sum+i
    count+=1
    if sum>=24:
        break
print("the numbers required to get sum or motre than 24 is",count)

#using continue print only different combinations
for i in range(5):
    for j in range(5):
        if i ==j:
            continue
        else:
            print(i,j)








