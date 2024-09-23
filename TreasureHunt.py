print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Start the journey
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue. Which color do you choose? \n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
elif choice1 == "right":
    print("You are at the village outskirts.")
    choice4 = input('There is a lake on the right side of the village. Where do you want to go? Type "village" or "lake" \n').lower()
    if choice4 == "village":
        print("You got attacked and killed by the villagers! Game Over.")
    elif choice4 == "lake":
        print("You took a boat and went to an island in the north.")
        choice5 = input('Do you want to go to the island or ignore it? Type "GotoIsland" or "IgnoreTheIsland" \n').lower()
        if choice5 == "gotoisland":
            print("You arrive at the island.")
            choice6 = input('You found a cave on the island. Do you want to go inside or explore the beach? Type "cave" or "beach" \n').lower()
            if choice6 == "beach":
                print("You found some clues on the beach! It leads you to the cave entrance again.")
                choice7 = input('Do you go into the cave now? Type "yes" or "no" \n').lower()
                if choice7 == "yes":
                    print("You found the treasure deep inside the cave! You Win!")
                else:
                    print("You ignored the cave and missed the treasure! Game Over.")
            elif choice6 == "cave":
                print("You found a treasure inside the cave! You Win!")
            else:
                print("You hesitated too long and got caught in a storm! Game Over.")
        else:
            print("You ignored the island and couldn't find the treasure! Game Over.")
    else:
        print("You failed to find the treasure! Game Over.")
else:
    print("You took the wrong path and fell into a pit. Game Over.")