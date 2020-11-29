print("welcome to game of picking")
print("pickup your choice in 1,2,3,4")
print("your choice should not be same always")
matchsticks=21
used_choice=[]
while matchsticks>=1:
    player = int(input("enter choice of user in 1,2,3,4: "))
    if player>4:
        print("in-valid entry")
        print("Game Over")
        break
    if player in used_choice:
        print("you had already used this choice")
        print(" Game  Over")
        break
    computer=player
    matchsticks=matchsticks-player-computer
    used_choice.append(player)
    if matchsticks==1:
        print("you have lost to computer")
        break
#how to stop the repeated values
