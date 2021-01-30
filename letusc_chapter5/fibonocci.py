def fibonocci(number):
    if number<=1:
        return number
    else:
        fibo=fibonocci(number-1)+fibonocci(number-2)
        return fibo
for i in range(1,26):
    print(fibonocci(i))

