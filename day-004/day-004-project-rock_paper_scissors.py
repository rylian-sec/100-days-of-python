# You are going to build a Rock, Paper, Scissors game. You will need to
# use what you have learnt about randomisation and Lists to achieve this.

# Demo
# https://appbrewery.github.io/python-day4-demo/

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# My code begins below:

import random

rock_paper_scissors = [rock, paper, scissors]

print("Choose Rock, Paper, or Scissors\n")
user_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
computer_choice = random.randint(0, 2)

#Added guard rail if statement

if user_choice > 2 or user_choice < 0:
    print("You have chosen and invalid number. You lost!")
else:
    print("You chose:\n")
    print(rock_paper_scissors[user_choice])

    print("\nI chose:\n")
    print(rock_paper_scissors[computer_choice])

if user_choice == 0:
    if computer_choice ==2:
        print("You won!")
    elif computer_choice == 0:
        print("It's a tie!")
    else:
        print("You lost!")

if user_choice == 1:
    if computer_choice ==0:
        print("You won!")
    elif computer_choice == 1:
        print("It's a tie!")
    else:
        print("You lost!")

if user_choice == 2:
    if computer_choice ==1:
        print("You won!")
    elif computer_choice == 2:
        print("It's a tie!")
    else:
        print("You lost!")
