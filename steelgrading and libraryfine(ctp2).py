#Grading of the Steel
hardness=int(input("enter hardness of steel"))
carbon_content=float(input("entervalue of carbon content"))
tensile_strength=int(input("enter value of tensile Strength"))
if hardness>50 and carbon_content>0.7 and tensile_strength>5600:
    print("the Grading of Steel is 10")
elif hardness>50 and carbon_content>0.7:
    print("the grading of steel is 9")
elif carbon_content>0.7 and tensile_strength>5600:
    print("the Grading of Steel is 8")
elif hardness>50 and tensile_strength>5600:
    print("The grading of Steel is 7")
elif hardness>50 or carbon_content>0.7 or tensile_strength>5600:
    print("The Grading of Steel is 6")
else:
    print("The Grading of steel is 5")
#library Fine
delayed_days=int(input("Enter the no of days delayed"))
if delayed_days in range(1,6):
    print("your fine for your delay in return of book is 50 Paise")
elif delayed_days in range(6,11):
    print("your fine for your delay in return of book is 1 Rupee")
elif delayed_days in range(11,31):
    print("your fine for your delay in return of book is 5 Rupee")
elif delayed_days>30:
    print("your membership is cancelled due to dealy in return of book for more than 30 days")
else:
    print("No fine")