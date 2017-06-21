
import random

"""
This is a simple version of the game mastermind.
The goal is to guess the 4 random colors.

Rules:
- The colors: red, blue, green, yellow, orange
- The code has only unique colors, no duplicates.
- Every position must have a color.
- After guessing the Codemaster gives hints.
    - black pin: Correct color and correct position.
    - white pin: Correct color but wrong position.

"""

def mastermind():
    tries = 0
    colors = {"red": "r",
              "blue": "b",
              "green": "g",
              "yellow": "y",
              "orange": "o"}
    codemaster = random.sample(list(colors.values()), 4)
    while tries <= 10:
        try:
            guess = list(input("Enter 4 colors as a guess: "))
        except ValueError:
            print("Invalid input.")



#  TODO: After a guess, give feedback


# TODO: If guess is correct, ask to play again

mastermind()