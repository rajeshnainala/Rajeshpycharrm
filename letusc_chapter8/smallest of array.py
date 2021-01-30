import array as arr
a=arr.array('d',[4.5,6.7,6.3,6.2,11.1,1.4])
min=a[0]
for i in range(len(a)):
    if  a[i]<min:
        min=a[i]
print("the minimum of array is: ",min)