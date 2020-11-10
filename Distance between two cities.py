distance=int(input("Enter the distance in km"))
meter=distance/1000
feet=distance/3281
inches=distance/39370
centimeter=distance/100
print("Distance between two Cities in Kilometers:",distance,"kms")
print("Distance between two Cities in Metres    :",meter,"mts")
print("Distance between two Cities in Feet      :",round(feet,5),"feet")
print("Distance between two Cities in Inches    :",round(inches,5),"inchs")
print("Distance between two Cities in Centimeters:",centimeter,"cms")