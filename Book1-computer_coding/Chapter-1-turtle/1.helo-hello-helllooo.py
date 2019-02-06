from random import randint
print()
print('hello world!')
print(randint(1,5))
def spaces_for_life():
    for i in range(3):
        print()

spaces_for_life()
feel_brave = True
while feel_brave:
    ghost_door = randint(1,5)
    door = input('1, 2, 3, 4, 5 ...........?')
    door_num = int(door)
    if door_num == ghost_door:
        print('Ghost Ghost Ghost .................')
        print('Have Fun lol :)')
        feel_brave = False
    else:
        print('Enter next room')
print("Run Away!!!")