
user_name = input("Enter Your Name \n:").lower()
# lover_name = input("Enter Your Lover's Name\n:")
alpha_true = ['t', 'r', 'u' , 'e', ]
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0


# if user_name[0]  == alpha_true[0] or [1] or [2] or [3]:
#     counter_1 += 1
# elif user_name[1]  == alpha_true[1] or [2] or [3] :
#     counter_2 += 1
# elif user_name[2]  == alpha_true[0] or [1] or [2] or [3]:
#     counter_3 += 1
# elif user_name[3]  == alpha_true[0] or [1] or [2] or [3]:
#     counter_4 += 1



if user_name[0]  == alpha_true[0]:
    counter_1 = counter_1 + 1
elif user_name[0]  == alpha_true[1]:
    counter_1 = counter_1 + 1
elif user_name[0]  == alpha_true[2]:
    counter_1 = counter_1 + 1
elif user_name[0]  == alpha_true[3]:
    counter_1 = counter_1 + 1

if user_name[1]  == alpha_true[0]:
    counter_1 = counter_1 + 1
elif user_name[1]  == alpha_true[1]:
    counter_1 = counter_1 + 1
elif user_name[1]  == alpha_true[2]:
    counter_1 = counter_1 + 1
elif user_name[1]  == alpha_true[3]:
    counter_1 = counter_1 + 1
    
if user_name[2]  == alpha_true[0]:
    counter_1 = counter_1 + 1
elif user_name[2]  == alpha_true[1]:
    counter_1 = counter_1 + 1
elif user_name[2]  == alpha_true[2]:
    counter_1 = counter_1 + 1
elif user_name[2]  == alpha_true[3]:
    counter_1 = counter_1 + 1 

else:
    print("Doe")

print(counter_1)



