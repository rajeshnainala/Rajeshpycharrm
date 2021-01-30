import array as arr
a=arr.array('i',[]) # declaring an array
n=int(input("enter length of array"))  # declaring length of array

def importing(b): #importing function to import values to array
    for i in range(n):
        x=int(input("enter a integer value: "))
        b.append(x)
    print("Before Sorting the Array elements",b)
def sorting(b): # sorting function to sort array elements
    for i in range(n-1):
        for j in range(i+1,n):
            if b[i]>b[j]:
                b[i],b[j]=b[j],b[i]
    print("After sorting the array elements",b)
importing(a)
sorting(a)