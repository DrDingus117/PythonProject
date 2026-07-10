import random

def guess_number():
    secret_number = random.randint(1, 10)

    # For testing/assignment purposes
    print("The secret number is:", secret_number)

    guess = 0

    while guess != secret_number:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess < 1 or guess > 10:
            print("Please guess a number between 1 and 10.")
        elif guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number:", secret_number)

guess_number()