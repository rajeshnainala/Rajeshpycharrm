def recfactorial(number):
    if number==1:
        return number
    else:
        factorial=number*(recfactorial(number-1))
        return factorial
number=int(input("enter a intger"))
print(recfactorial(number))