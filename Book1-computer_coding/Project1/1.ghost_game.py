import random

print("")
print(" This is the GHOST Game!!!")
print("")

feeling_brave = True
score = 0

while feeling_brave:
    ghost_door = random.randint(1, 5)
    print(" hey guys there are 5 doors ahead !!!")
    print(" In one of the doors the ghost is there :( :( :( ")
    print(" Which door do you want to open select that one!!!")
    number=input('1, 2, 3, 4 or 5?')
    door_num=int(number)
    if door_num == ghost_door:
        print("")
        print("Ghost found!!!")
        feeling_brave = False
    else:
        print("  Ghost Not found!!!")
        print("")
        print("  You enter the next Room to see the Ghost")
        print("")
        score = score + 1
print("")
print("Run Away!!!")
print("Game Over!!! You scored", score)


