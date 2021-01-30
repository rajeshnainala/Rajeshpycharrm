def rec_sum(number):
    if number<=1:
        return number
    else:
        sum=number+rec_sum(number-1)
        return sum
print(rec_sum(25))