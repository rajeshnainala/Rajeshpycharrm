#with out recursion
def sodigits(number):
    sum=0
    last_digit=0
    while number!=0:
        last_digit=number%10
        sum+=last_digit
        number=number//10
    return sum
number=int(input("enter five digit number"))
print(sodigits(number))

#with recursion
def recsodigits(number2):
    if number2==0:
        return number2
    else:
        last=number2%10
        sum2=last+recsodigits(number2//10)
        return sum2
number2=int(input("enter five digit integer"))
print(recsodigits(number2))