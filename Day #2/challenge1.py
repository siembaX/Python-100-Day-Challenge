""" 
Here is a chalalenge to accept input of only a single 2 digit
number, then we add this number, e.g. 23 => 2 + 3 = 5
So the expected number will be 5
"""

print('Welcome to input caluculator');
user_num = input('Enter a 2 digit number:\n')
int(user_num)
print(type(user_num))
num_1 = user_num[0]
num_2 = user_num[1]

print(int(num_1) + int(num_2))




