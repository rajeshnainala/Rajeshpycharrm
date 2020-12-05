age=int(input("enter the age of person"))
health_conditon=input("enter health condition is poor/excellent").lower()
locality=input("enter whether person live in city/village").lower()
gender=input("enter gender of a persons").lower()

if age in range(25,35):
    if health_conditon=='excellent' and locality=='city':
        if gender=='male':
            print("The person is eligible for insurance of  premium  Rs 4 and policy cannot exceed rs 2 lakhs")
        elif gender=='female':
            print("The person is eligible for insurance of premium Rs 3 and policy cannot exceed Rs 1 lakh")
        else:
            print('the person is not eligible for insurance')
    elif health_conditon=='poor' and locality=='village' and gender=='male':
        print("The person is eligible for insurance of premium Rs 6 and doesnot exceed Rs 10,000")
    else:
        print("The person is not eligible for insurance")
else:
    print("The person is not eligible for insurance")