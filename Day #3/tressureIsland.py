print("\033c")

print('''Welcome to Tressure Island.
Your mission is to find tressure. 

''')

Player_Choice = input("As you are walking you come to a cross road, which route do you take \nLEFT or RIGHT? ").lower()
if Player_Choice == "left":
    Player_Choice2 = input("As you travel, along the way you see a river do you\n SWIM or WAIT ").lower()
    if Player_Choice2 == "wait":
        Player_Choice3 = input("Which door do you pick\n RED or BLUE? ").lower()
        if Player_Choice3 == "red":
            print("You got consumed by Bears")     
        elif Player_Choice3 == "blue":
            print("Eureka, You Win!")
        else:
            print("The building fell off the ground and crushed you")
    else:
        print("Ohh no, crocodiles, Game Over!!!")
else:
    print("hahaha you should know best not to choose RIGHT")