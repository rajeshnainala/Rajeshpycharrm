def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact=fact*i
        i+=1
    print("factorial of given number",n,"is",fact)
factorial(int(input("enter an integer")))