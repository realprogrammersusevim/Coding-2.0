# Hangman game.
# TODO: Problem 1. The guessed character is never triggered as being equal to the current character it's being checked
#  against. Perhaps "char" is the wrong term for what I mean?

import os

the_word = input("What should the secret word be? ").lower()
number_of_tries = int(input("How many tries should the guessers get? "))

while number_of_tries < 1:
    print("The number of tries needs to be 1 or more.")
    number_of_tries = int(input("How many tries should the guessers get? "))

blank_word = ""
for char in the_word:
    blank_word += " "


def guess_function():
    characters_in_guess = 0

    guess = input("What is your guess? ").lower()

    for char in guess:
        characters_in_guess += 1
    if characters_in_guess > 1:
        print("Just one letter!")
        guess_function()


print("You're all set up! Let the game begin.")

while number_of_tries > 0:
    correct_guess = False
    guess_function()
    index_position = 0

    for char in the_word:
        index_position += 1

        if guess == char:
            temporary = list(blank_word)
            temporary[index_position] = guess_function
            blank_word = "".join(temporary)

            correct_guess = True
        # Here I'm putting the correctly guessed character into the blank string at the correct index. As the player
        # guesses the correct words the blank spaces will be filled with the correct letters to form the word.

    if not correct_guess:
        number_of_tries -= 1
        print("Here's the guessed word so far: " + blank_word)
    elif correct_guess:
        if blank_word == the_word:
            print("Hey! You won!")
            print(blank_word + " was the secret word!")
            break
        else:
            print("Here's the guessed word so far: " + blank_word)

if number_of_tries == 0:
    print("Sorry, you lost.")

answered_the_question = False
play_again = input("Would you like to play again? (y/n) ")

while not answered_the_question:
    if play_again == "y":
        os.system("python3 /Users/admin/Desktop/Hangman.py")
        answered_the_question = True
    elif play_again == "n":
        print("See you next time then.")
        answered_the_question = True
    else:
        print("Hmm, you didn't answer the question as requested.")
