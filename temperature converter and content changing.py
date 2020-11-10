'''Temperature of a city in Fahrenheit degrees is input through
the keyboard. Write a program to convert this temperature
into Centigrade degrees'''

fahrenhiet=float(input("enter the value of temperature in fahrenhiet"))
celsius=(fahrenhiet-32)*5/9
print("Temperature in Fahrenhiet Scale: ",fahrenhiet,"F")
print('Temeperaturen in Celsius Scale: ',round(celsius,2),"C")

'''Two numbers are input through the keyboard into two
locations C and D. Write a program to interchange the
contents of C and D'''


c=input("Enter a value to c")
d=input('Enter a value to d')
print("The value in C before Swaping:",c)
print("The value in D before Swaping",d)
temp=0
temp=c
c=d
d=temp
print("The value in C after Swaping: ",c)
print("The value in D after Swaping:",d)