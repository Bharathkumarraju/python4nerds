
def spaces():
    for i in range(5):
        print()
spaces()
age = input('whats the age?')
print("The age is ", age)
spaces()


a = 2.1

if a == 2:
    print("Hello")
else:
    print("good bye!!!")
    print("")

for i in range(10):
    print("SRi Anjaneyam!!! Prasanna Anjaneyam!!!")

spaces()

word='dragon'

if word == 'dragon':
    print("you are from china")
elif word == 'elephant':
    print("you are from india")
else:
    print("I don't know from which fucking country you are!!!")

spaces()
roll = 0

while roll != 6:
    print(" Roll is not equal to 6, the roll value is ", roll)
    roll += 1



from time import sleep
print("I am going to sleep for 2 seconds")
sleep(2)

print("I am awaken now and I am chanting hanuman chalisa now!!!")

# How to greet using finctions

def greet(abc:str='hanuman'):
    print("Hello " + abc)

greet('raju')
greet()