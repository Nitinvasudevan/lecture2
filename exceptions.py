import sys

try:
    x = int(input("X: "))
    y = int(input("Y: "))
except ValueError:
    print("Please enter a number")
    sys.exit(1)
    
try:
    result = x/y
except ZeroDivisionError:
    print("Error dividing by Zeeeeeeero")
    sys.exit(1)

print (f"{x} / {y} = {result}")