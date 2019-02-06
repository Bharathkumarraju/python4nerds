from random import randint
print('Ghost Game!!!')
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint(1, 3)
    print('Three doors ahead ...')
    print('A ghost behind one.')
    print('Which door do you open?')
    door = input('1, 2, or 3? ')
    door_num = int(door)
    if door_num == ghost_door:
        print('GHOST..............')
        feeling_brave = False
    else:
        print('No Ghost')
        print('Enter the Next Room...')
        score = score + 1
print('Run Away!!!')
print('Game Over! You scored', score)