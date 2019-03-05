age = input('whats your age?')
print("")
print("The type of object age is ")
print(type(age))
print("")

my_age = int(age)

print("")
print("using comma to display the age")
print("The age is ", my_age)
print("The age is ", age)

print("")
print("using plus display the age")
print("THE AGE IS " + age)
# print("THE AGE IS " + my_age), It throws error, TypeError: can only concatenate str (not "int") to str
try:
    print("THE AGE IS " + my_age)
except Exception as err:
    print(err)

