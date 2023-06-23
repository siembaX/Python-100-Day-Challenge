print("\033c")

""" 
My Program checks if a year is a leap year
"""

year = int(input("Enter the desired Year:"))

if year % 4 == 0 and year % 400 == 0: 
    print("Is a leap year")
elif year % 4 == 0 and year % 400 != 0 and year % 100 != 0 : 
    print("Is a leap year")
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
    print("Not a leap year")
else:
    print("not a leap year")
