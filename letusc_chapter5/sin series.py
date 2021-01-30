def sin_series(number):
    sinx=0
    for i in range(5):
        sinx+=pow(-1,i)*(pow(number,((2*i)+1))/factorial((2*i)+1))
    return round(sinx,2)
def factorial(n):
    if n==1:
        return n
    else:
        fact=n*(factorial(n-1))
        return fact

print(sin_series(2))