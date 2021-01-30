def prime_factor(number):
    prime_fc=2
    while number>1:
        while number%prime_fc==0:
            print(prime_fc,end=' ')
            number=number//prime_fc
        prime_fc+=1
prime_factor(number=int(input("enter a positive inger: ")))


