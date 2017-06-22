
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

    colors = {"r": "Red",
              "b": "Blue",
              "g": "Green",
              "y": "Yellow",
              "o": "Orange"}
    codemaster = random.sample(list(colors.keys()), 4)

    while tries <= 10:
        try:
            guess = list(input("Your guess: "))
            if len(set(guess)) != 4:
                raise ValueError
            if not set(guess) == set(i for i in colors.keys() if i in guess):
                raise ValueError
        except ValueError:
            print("Invalid input. \n")
            continue
        print("-"*35)
        print("You chose: 1: {}, 2: {}, 3: {}, 4: {}".format(colors[guess[0]], colors[guess[1]], colors[guess[2]], colors[guess[3]]))

        if guess == codemaster:
            print("You cracked the code! Congratulations!")
            break
        else:
            black_pin = 0
            white_pin = 0
            for color in range(4):
                if guess[color] == codemaster[color]:
                    black_pin += 1
                elif guess[color] != codemaster[color] and guess[color] in codemaster:
                    white_pin += 1
            print("{} black pins. {} white pins. \n".format(black_pin, white_pin)+ "-"*25)
        tries += 1


# TODO: If guess is correct, ask to play again

mastermind()
