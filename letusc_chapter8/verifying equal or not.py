import array as arr
a=arr.array('i',[2,3,4,5,6,4,3,2])
b=arr.array('i',[9,89,1,3,6,5,4,7])
def equal_not(c):
    for i in range(len(c)):
        if a[i]==a[len(c)-(1+i)]:
            print("the value in",i," position is equal to value in",len(c)-1-i)
        else:
            print("not equal")
equal_not(a)
