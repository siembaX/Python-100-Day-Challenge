""" Existance on Planet Earth for 90 Years of your life """

age = input("Enter your age: ")

lifeTime = 90 - int(age)
print(lifeTime)

days = lifeTime * 365
weeks = lifeTime * 52
months = lifeTime * 12

print(f"You have {days} days, {weeks} weeks, and {months} months on earth")

