import array as arr
a=arr.array('i',[2,3,5,4,6,8,9,10,1,0,7])
def multiply(b):
    for i  in range(len(b)):
        b[i]=b[i]*3
    return b
print(multiply(a))