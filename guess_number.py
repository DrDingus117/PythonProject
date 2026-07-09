## 1. Generate a random number between 1 and 10
## 2. Ask the user to guess the number
## 3. If the guess is too high, tell the user to guess lower
## 4. If the guess is too low, tell the user to guess higher
## 5. If the guess is correct, tell the user they won

import random
secret_number: int = random.randint(1, 10)

def number_guessing_game():
    secret_number: int = random.randint(1, 10)
    guess: int = 0
    
    while guess != secret_number:
        guess_input: int = int(input("Guess a number between 1 and 10: ").strip())
        
        if not 1 <= guess_input <= 10:
            print("Invalid input. Please guess a number between 1 and 10.")
            continue
        
        guess = int (guess_input)
        
        if not 1 <= guess <= 10:
            print("Please guess a number in the range of 1 and 10.")
            continue
        
        if guess_input < secret_number:
            print("Too low! Try again.")
        elif guess_input > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number:", secret_number)

guess_number()