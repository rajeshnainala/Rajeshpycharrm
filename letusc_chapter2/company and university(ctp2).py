#Worker capability
hours=float(input("Time taken by person to complete work"))
if hours>2 and hours<=3:
    print("The worker is highly efficient")
elif hours>3 and hours<=4:
    print("The worker is orderes to improve speed")
elif hours>4 and hours<=5:
    print("The worker is given training to inmprove speed")
elif hours>5:
    print("The worker is asked to leave company")
else:
    print("Wrong entry")

#Student Capability
a=int(input("marks obtained in subject A"))
b=int(input("marks obtained in subject B"))

if a>=55 and b>=45:
    print("The student is Qualified")
elif 45<a<=55 and b>=55:
    print("The student is Qualified")
elif a>=65 and b<45:
    print("The student have to reappear in exam B")
else:
    print("The Student is failed")

#order supply
stock=int(input("enter stock avilable"))
order=int(input("enter order by customer"))
credit=input("enter whether his/her credit is ok in y/n").lower()
if order<=stock and credit=='y':
    print("your order is supplied")
elif order>stock and credit=='y':
    print("we supplied ",stock,"as per your order and reamining",order-stock,"will be supplied later")
elif credit=='n':
    print("to get your order pleaseforst clear the credit")
else:
    print("wrong entry")


