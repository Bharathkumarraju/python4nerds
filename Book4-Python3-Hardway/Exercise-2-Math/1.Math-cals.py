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

'''

try:
    1/0
except:
    err1 = sys.exc_info()
    for i in err1:
        print(i)
