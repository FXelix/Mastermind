
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

    colors = {"r": "red",
              "b": "blue",
              "g": "green",
              "y": "yellow",
              "o": "orange"}
    codemaster = random.sample(list(colors.keys()), 4)

    while tries <= 10:
        try:
            guess = list(input("Enter 4 colors as a guess: "))
            if len(set(guess)) != 4:
                raise ValueError
            if not set(guess) == set(i for i in colors.keys() if i in guess):
                raise ValueError
        except ValueError:
            print("Invalid input. Example input: gbyo")
            continue

        print("You chose: 1: {}, 2: {}, 3: {}, 4: {}".format(colors[guess[0]], colors[guess[1]], colors[guess[2]], colors[guess[3]]))

        if guess == codemaster:
            print("You cracked the code! Congratulations!")
            break
        else:
            for color in range(4):
                if guess[color] == codemaster[color]:
                    print("One black pin.")
                elif guess[color] != codemaster[color] and guess[color] in codemaster:
                    print("One white pin.")
        tries += 1


#  TODO: Print pretty feedback


# TODO: If guess is correct, ask to play again

mastermind()