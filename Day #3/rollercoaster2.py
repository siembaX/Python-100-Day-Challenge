print("\033c")

height = (int(input("What is your height (m) :")))
if height >= 120:
    print("You can ride the cart")
    age = (int(input("what is your age :")))


if age <= 55 and age >=45:
    print("You pay $0")
elif age <= 18 and age >= 12:
    print("You pay $7")
elif age <= 12 and age >= 1:
    print("Print $5")
else:
    print("Not a supported value!!")
