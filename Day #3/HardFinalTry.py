print("\033c")

user_name = input("Your Name \n:").lower()
lover_name = input("Lover's Name \n:").lower()

letter1 = user_name.count('t')
letter2 = user_name.count('r')
letter3 = user_name.count('u')
letter4 = user_name.count('e')
letter5 = user_name.count('l')
letter6 = user_name.count('o')
letter7 = user_name.count('v')
letter8 = user_name.count('e')

letter_set1 = letter1 + letter2 + letter3 + letter4 +letter5 + letter6 + letter7 + letter8

letter1 = lover_name.count('t')
letter2 = lover_name.count('r')
letter3 = lover_name.count('u')
letter4 = lover_name.count('e')
letter5 = lover_name.count('l')
letter6 = lover_name.count('o')
letter7 = lover_name.count('v')
letter8 = lover_name.count('e')

letter_set2 = letter1 + letter2 + letter3 + letter4 +letter5 + letter6 + letter7 + letter8
total_match = (str(letter_set1)) + (str(letter_set2))

total_match_int = (int(total_match))

if total_match_int <=10 or total_match_int >=90:
    print(f"Your Score is {total_match_int}, you go together like coke and mentos")
elif total_match_int >=40 and total_match_int <= 50:
    print(f"Your Score is {total_match_int}, you are alright together.")
else:
    print(f"Hmmm weird match, your score is {total_match_int}")