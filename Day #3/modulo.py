""" 
Diving numbers and returning the remainder
e.g 7 % 2 = 1
"""

digit = int(input("Please your number\n:"))

result = digit % 2

if result == 0:
    print("Is even")
else:
    print(f"Your result is {result}")

