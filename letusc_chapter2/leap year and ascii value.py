#leap year
year=int(input("enter any year"))
if (year%4==0 or year%400==0) and year%100!=0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")

#ascii value
character=input("enter a character")
asci=ord(character)
if asci>=65 and asci<=90:
    print("the character",character,"is capital alphabetic letter")
elif asci>=97 and asci<=122:
    print("the character",character,"is small alphabetic letter")
elif asci>=48 and asci<=57:
    print("the character",character,"is a digit")
elif 0<=asci<=47 or 58<=asci<=64 or 91<=asci<=96 or 123<=asci<=127:
    print("the character, character, is a symbol")
else:
    print("Wrong entry")
