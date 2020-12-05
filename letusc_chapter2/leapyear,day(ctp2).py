year=int(input("Enter a year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year," is a leap Year")
        else:
            print(year," is not a leap year")
    else:
        print(year," is a leap Year")
else:
    print(year,"is a leap year")

# to find the day
year=int(input("enter a year"))
initial_year=1900
years=(year-1)-initial_year
leap_years=years//4
non_leap_years=years-leap_years
no_of_days=(non_leap_years*365)+(leap_years*366)+1
if no_of_days%7==0:
    print("1st janauryof the ",year,"is Monday")
elif no_of_days%7==1:
    print("1st janauryof the ", year, "is Tuesday")
elif no_of_days%7==2:
    print("1st janauryof the ", year, "is Wednesday")
elif no_of_days%7==3:
    print("1st janauryof the ", year, "is Thursday")
elif no_of_days%7==4:
    print("1st janauryof the ", year, "is Friday")
elif no_of_days%7==5:
    print("1st janauryof the ", year, "is Saturday")
elif no_of_days%7==6:
    print("1st janauryof the ", year, "is Sunday")
else:
    print("Entered year is wrong")