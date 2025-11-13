import random

print(" Welcome to Devang's Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it!\n")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("The number is higher than the number you guessed.\n")
    elif guess > secret_number:
        print("The number is lower than the number you guessed.\n")
    else:
        print(f"Correct! The number was {secret_number}.")
        print(f"You guessed it in {attempts} attempts!")
        break 