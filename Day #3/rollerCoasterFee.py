""" 
This Program code calculates the rollercoaster fee based on age,
It also checks elligability based on height
"""

height = int(input("Please specify height \n: "))
age = int(input("Please specify age \n: "))
adult_price = 12
kids_price = 7

# if height > 120:
#     print("Elligible Height, You can Proceed")
# elif age <= 18:
#     print(f"Your price is {kids_price} and you pay less")
# elif age >= 18:
#     print(f"Your price is {adult_price} and you pay more");       
# else:
#     print("You're not elligable for your height")
    
if height >= 120 and age >= 18:
    print(f"Elligible Height, Your Price is {adult_price} and you pay more")
elif height >= 120 and age <= 18:
    print(f"Your Price is {kids_price} and you pay less")
elif height <= 120 and age >= 18:
    print(f"Your height is not supported but your price is {adult_price} and you more")
else:
    print("Your height is low and youre underage")
    
