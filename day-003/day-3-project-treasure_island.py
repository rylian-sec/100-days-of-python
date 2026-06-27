#Your goal today is to build a "Chose your own adventure game". Using what you
# have learnt in the lessons today you will be building a very simple version of
# this type of text game.

# Use the flow chart linked here to create the game logic.
#https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D

#Once you've completed the project, you can always extend the game and make it
# more interesting!

#==============================================================================

print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the treasure.\n")

#==============================================================================

# My code, for project completion, begins here.

direction_choice = input("You can go left or right.\nEnter L or R: ").lower()

if direction_choice == "l":
    print("\nYou walk for a few hours and....")
    print("You have come to a dock on a beautiful and vast lake, with an island in the middle.\n")
    swim_or_wait = input("Would you like to Swim across or Wait for a boat? \nEnter S or W: ").lower()

    if swim_or_wait == "w":
        print("\nA boat arrives and ferries you to the island.")
        print("In the center of the island is a small building with three doors, one Red, one Yellow, and one Blue.\n")
        door_choice = input("Which would you like to open? \nEnter R, B, or Y: ").lower()

        if door_choice == "y":
            print("\nYou found the treasure! You Win!")
        elif door_choice == "r":
            print("\nA fireball envelopes you.\nGame Over.")
        elif door_choice == "b":
            print("\nA giant tiger jumps out and eats you.\nGame Over.")
        else:
            print("\nThat is not a valid door. Game Over.")

    else:
        print("\nA giant trout swallows you whole.\nGame Over.")

else:
    print("You fall into a deep hole. \nGame Over.")