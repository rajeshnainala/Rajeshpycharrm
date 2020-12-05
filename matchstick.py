print("welcome to game of picking")
matchsticks=21
while matchsticks>1:
    user_choice = int(input("enter choice of user in 1,2,3,4: "))
    computer_choice=5-user_choice
    matchsticks=matchsticks-(user_choice+computer_choice)
if matchsticks==1:
    print("you have lost to computer")

