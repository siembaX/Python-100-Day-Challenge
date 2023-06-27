print("\033c")

name = input("Enter Your Name:\n")
lover_name = input("Lover's Name:\n")

combined = name + lover_name
lowerCase = combined.lower()

t = lowerCase.count('t')
r = lowerCase.count('r')
u = lowerCase.count('u')
e = lowerCase.count('e')

true = t + r + u + e

l = lowerCase.count('l')
o = lowerCase.count('o')
v = lowerCase.count('v')
e = lowerCase.count('e')

love = l + o + v + e

total_love = str(true) + str(love)
print(total_love)
true_love_int = int(true_love)
 
print(true_love_int)


if true_love_int <=10 or true_love_int >=90:
    print(f"Your Score is {true_love_int}, you go together like coke and mentos")
elif true_love_int >=40 and true_love_int <= 50:
    print(f"Your Score is {true_love_int}, you are alright together.")
else:
    print(f"Hmmm weird match, your score is {true_love_int}")