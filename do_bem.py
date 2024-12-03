import random

number = random.randint(1, 10)

try:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == number:
        print("You won!")
    else:
        print(f"You lost! The correct number was {number}. Try again!")
except ValueError:
    print("Invalid input. Please enter a valid number.")
