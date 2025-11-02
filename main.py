'''
       NUMBER GUESSING GAME

This Python program lets the user guess a randomly generated number 
between 1 and 10 with a maximum of 5 attempts.

-Game Rules:
    1. The program generates a random number (1-10).
    2. The user must guess the number within 5 attempts.
    3. After each guess:
        - If correct → display a congratulatory smiley image and end game.
        - If too low or too high → display a hint.
    4. If the user fails in 5 attempts → display an angry smiley image.

-Libraries:
    1. 'random
    2. 'Pillow(PIL)' - for displaying images

-Return Type: bool
'''

import random
from PIL import Image

# Step 1 & 2: Start the game and generate random number
print(" Welcome to the Number Guessing Game!")
SecretNumber = random.randint(1, 10)
MaxAttempts = 5
Attempt = 0

# Step 3 to 6: User guesses loop
while Attempt < MaxAttempts:
    Guess = int(input(f"Attempt {Attempt}/{MaxAttempts} → Enter your guess (1-10): "))
    # Check for invalid input
    if Guess < 1 or Guess > 10:
        print(" Invalid input! Please enter a number between 1 and 10.")
        continue  

    Attempt += 1 


    if Guess == SecretNumber:
        print(" Correct! You guessed the number!")
        # Step 4: Show congratulatory smiley
        img = Image.open("Happy.jpg")   
        img.show()
        break
    elif Guess < SecretNumber:
        print("Too low!  Try again.")
    else:
        print("Too high! Try again.")

    # Step 7: If attempts are over
    if Attempt == MaxAttempts:
        print(f"Game Over! The number was {SecretNumber}.")
        # Show angry smiley
        img = Image.open("Angry.jpg")
        img.show()
