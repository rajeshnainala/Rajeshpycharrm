def rec_binary(number):
    if number==0:
        return number
    else:
        remainder=(number%2)
        binary=(remainder)+(10*rec_binary(number//2))
        return binary
number=int(input("enter a positive integer"))
print((rec_binary(number)))
