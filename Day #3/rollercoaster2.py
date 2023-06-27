print("\033c")

height = (int(input("What is your height (m²) :")))
if height >= 120:
    age = (int(input("what is your age :")))


if age >= 18  and age <= 45:
    print("You pay $12")
    bill = 12
elif age <= 55 and age >=45:
    print("You pay $0")
    bill = 0
elif age <= 18 and age >= 12:
    print("You pay $7")
    bill = 7
elif age <= 12 and age >= 1:
    print("Print $5")
    bill = 5
else:
    print("Not a supported value!!")
    
photoshoot = input("Do you want a portrait taken? \nY or N:")
if photoshoot == "Y":
    bill += 6
    print(f"Your Total Bill is: ${bill}")
    
    