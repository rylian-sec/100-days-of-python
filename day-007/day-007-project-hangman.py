# This is my code for the day 7 project, Hangman.

from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages
import random

placeholder = ""
correct_guess = []
game_over = False
lives = 6

print(logo)

chosen_word = random.choice(word_list)
# print(chosen_word)


for _ in chosen_word:
    placeholder += "_ "

print(placeholder)

while not game_over:

    print(f"You have {lives}/6 lives left.")
    player_guess = input("Guess a letter: ").lower()

    display = ""

    if player_guess in correct_guess:
        print(f"You've already guessed {player_guess}. Try again.")

    for letter in chosen_word:
        if letter == player_guess:
            display += letter + " "
            correct_guess.append(player_guess)
        elif letter in correct_guess:
            display += letter + " "
        else:
            display += "_ "

    if player_guess not in chosen_word:
        print(f"Sorry, {player_guess} is not in the word.")
        lives -= 1

    print(display)

    if lives == 0:
        game_over = True
        print(f"The word was {chosen_word}! You lose!")

    if "_ " not in display:
        game_over = True
        print("You win!")

    print(stages[lives])


