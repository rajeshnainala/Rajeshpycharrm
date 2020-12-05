student_name=("enter the student name")
maths=int(input("enter the marks obtained in maths"))
science=int(input("enter the marks obtained in scienc"))
social=int(input("enter the marks obtained in social"))
english=int(input("enter the marks obtained in english"))
hindi=int(input("enter the marks obtained in hindi"))

total_aggregate=maths+science+social+english+hindi
percentage=(total_aggregate/500)*100
print(student_name,"Marks List:")
print("****************************")
print("Marks Obtained in Maths:   ",maths)
print("Marks Obtained in Science: ",science)
print("Marks Obtained in Social:  ",social)
print("Marks Obtained in English:",english)
print("Marks Obtained in Hindi:",hindi)
print("****************************")
print("Total Aggregate       :",total_aggregate)
print("Percentage Obtained   :",percentage,"%")

