import sys
print("")
print("Let's count")

print("hens", 35 + 10*6/2 )
print("roosters", 100 - 25 * 3 % 4)

print(" Now  I will count the eggs!!!")
print(3 + 2 - 5 * 9 % 3 * 99 / 2 + 199 )

try:
  print(1/0)
except Exception as err:
    print("Are you really want to division by fucking ZERO? Really?", str(err))
print("\n"*5)

'''
exc_info() returns three values tuple
1. First value indicates the exception type
2. Second details teh exception type
3. Third contains the traceback object that provides the access to the traceback message

The example output as below

<class 'ZeroDivisionError'>
division by zero
<traceback object at 0x102da85c8>

turkey airport

User Code: 595215
Password: 052274

'''

try:
    1/0
except:
    err1 = sys.exc_info()
    for i in err1:
        print(i)

print()
print("----------------------MATH CALCULATIONS---------------------")

print("the value is", 2*3*9+29999/10000)
print("is it true that 3 + 2 < 5 - 7 ?")
print(3 + 2 < 5 - 7)

print("What is 3 + 2 is", 3 + 2)
print("What is 5 - 7 is", 5 - 7)
print(" Oh That's why it is False")

