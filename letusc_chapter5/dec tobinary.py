def dec_to_binary(number):
    place=1
    binary=0
    while number!=0:
        remainder=number%2
        binary+=(remainder*place)
        place=place*10
        number=number//2
    return binary
print(dec_to_binary(30))
