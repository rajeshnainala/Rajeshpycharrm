def greatest_common_divisor(a,b):
    while b!=0:
        c=b
        b=a%b
        a=c
        if b==0:
            break
    return a
print(greatest_common_divisor(1980,1617))
