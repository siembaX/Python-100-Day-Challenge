""" 
My Program checks if a year is a leap year
"""

year = int(input("Enter the desired Year:"))

if year % 4 == 0: 
    if year % 100 == 0:
        if year % 400 == 0:
            print("Is a leap year")
        else:
            print("not a leap year")    
    elif year % 400 == 0:
        print("Is a leap year")
else:
    ("Not a leap Year")