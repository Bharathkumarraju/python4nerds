import random

print("")
print(" This is the GHOST Game!!! ")

score = 0

feeling_brave = True

while feeling_brave:
    print(" There are Five doors ahead! ")
    print(" There is a GHOST in one of the door! ")
    ghost_door = input(" Please selects the door 1, 2, 3, 4, or 5?")
    ghost_door_num = int(ghost_door)
    door = random.randint(1, 5)
    if ghost_door_num == door:
        print("")
        print(" GHOST has been found!!!")
        print(" Alas Please save me!")
        feeling_brave = False
    else:
        print("")
        print(" Ghost is not there please go ahead select another door! ")
        score = score + 1
print(" RUN Away, The ghost game has been over and your score is ")
print(" You have scored ", score)
