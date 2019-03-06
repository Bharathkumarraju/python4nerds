rabbits = 5
hats = rabbits

print("")
print(rabbits, hats)

sheep = 10
sheep_weight = 10.0123

print("")
print(sheep, sheep_weight)
print("")

# Strings includes letters, numbers, spaces, and symbols such as full stops and commas.
# They are usually put inside single quote marks.

a = "Coding is fun! isn't it?"
print(a)

x = True
y = False
print(x , y)
print("")

print(type(24))
print(type('24'))
print(type(24.5609234))
print(type(x))
print(type(False))
print("")

# Converting Data Types
# So variable contain any type of data , Problems occur if you try to mix types together.
# Data types sometimes have to be converted, otherwise an error message will appear.

apple = input('Enter number of apples')
print("")
print(type(apple))
try:
    print(apple + 1)
except Exception as err:
    print(err)
# In order to fix above first convert apple to int as below
print(int(apple) + 18)
