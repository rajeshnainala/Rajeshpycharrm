amount=int(input("enter the amount in hundreds"))
hdnotes=amount//100
r_amount_hd=amount-(100*hdnotes)
if r_amount_hd >= 50:
    ftnotes=(amount%100)//50
else:
    ftnotes=0
r_amount_ft=r_amount_hd-(50*ftnotes)

if r_amount_ft>=10:
    tnnotes=((amount%100)%50)//10
else:
    tnnotes=0
remaining_amount=r_amount_ft-(10*tnnotes)
print("No of 100 Notes is : ",hdnotes)
print("No of 50 Notes is: ",ftnotes)
print("No of 10 Notes is: ",tnnotes)
print("the Remaining amount is: ",remaining_amount)