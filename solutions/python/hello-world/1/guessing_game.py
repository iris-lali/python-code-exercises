# This is a guess the number game.
# This program prompts the user to guess a number between 1 and 100.

import random

low = 1
high = 100

guesses = 0

secret_number = random.randint(low, high)


while True:
    guess = int(input(f"Enter a number between {low} - {high} "))
    guesses += 1

    if guess < secret_number:
        print(f"{guess} is too low")
    elif guess > secret_number:
        print(f"{guess} is too high")
    elif guess == secret_number:
        print(f"{guess} is correct!")
        break

print(f"This round took you {guesses} guesses!")