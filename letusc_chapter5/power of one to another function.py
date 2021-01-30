import math
def power(a,b):
    c=math.pow(a,b)
    print("the power of",a,"to",b,"is",int(c))
power(int(input("enter value of a: ")),int(input("enter value of b: ")))