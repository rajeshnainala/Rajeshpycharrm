def circular_shift(a,b,c):
    temp=0
    temp=c
    c=b
    b=a
    a=temp
    return a,b,c
print(circular_shift(5,8,10))