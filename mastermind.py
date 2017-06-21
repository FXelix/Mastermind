
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
            if len(guess) != 4:
                raise ValueError
            elif not all(guess) in colors.values():
                raise ValueError
        except ValueError:
            print("Invalid input. Example input: gbyo")
            continue

        if guess == codemaster:
            print("You cracked the code! Congratulations!")
            break
        else:
            for color in range(4):
                if guess[color] == codemaster[color]:
                    print("One black pin.")
                elif guess[color] != codemaster[color] and guess[color] in codemaster:
                    print("One white pin.")


#  TODO: After a guess, give feedback


# TODO: If guess is correct, ask to play again

mastermind()