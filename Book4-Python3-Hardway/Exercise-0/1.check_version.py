import sys
import platform

def spaces():
    for i in range(3):
        print()

spaces()
print(platform.python_version())
spaces()
print(sys.version_info)
spaces()
print(sys.version)

