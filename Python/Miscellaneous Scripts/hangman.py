from getpass import getpass

the_word = getpass("Enter the word: ").lower()
the_word = list(the_word)
number_of_tries = int(input("How many tries should the guessers get? "))

while number_of_tries < 1:
    print("The number of tries needs to be 1 or more.")
    number_of_tries = int(input("How many tries should the guessers get? "))

guessed_letters = []
correct_letters = []

while number_of_tries > 0:
    if len(correct_letters) == len(the_word):
        print("You won!")
        print(f"The word was {''.join(the_word)}")
        break

    print(f"You have {number_of_tries} tries left.")
    for letter in the_word:
        if letter in guessed_letters:
            print(letter, end="")
        else:
            print("_", end="")
    print()

    guess = input("What is your guess? ").lower()
    if guess in guessed_letters:
        print("You have already guessed that letter.")
    elif guess in the_word:
        print("You guessed correctly!")
        guessed_letters.append(guess)
        correct_letters.append(guess)
    else:
        print("You guessed incorrectly.")
        guessed_letters.append(guess)
        number_of_tries -= 1

if number_of_tries == 0:
    print("You have run out of tries.")
    print(f"The word was {''.join(the_word)}.")
