#profit or loss

selling_price=int(input("enter selling price of a product"))
cost_price=int(input("enter cost price of a product"))
if selling_price>cost_price:
    profit=selling_price-cost_price
    print("the seller made a profit of  ",profit,'rupees')
elif cost_price>selling_price:
    loss=cost_price-selling_price
    print("the seller made a loss of ",loss,'rupees')
else:
    print("there is niether profit nor loss")

#odd or even

number=int(input("enter a integer value"))
if number%2==0:
    print("the Number",number,"is Even")
else:
    print("the Number",number,"is Odd")

#Reverse and Original are same or not

org_number=int(input("Enter a value"))
rev_number=0
exact_number=org_number
while org_number>0:
    a=org_number%10
    rev_number=(rev_number*10)+a
    org_number=int(org_number/10)
if rev_number==exact_number:
    print("the reverse and original number are equal")
else:
    print("the reverse and original number are not equal")

