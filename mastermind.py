
import random

"""
This is a simple version of the game mastermind.
The goal is to guess the 4 random colors.

Rules:
- The colors: red, blue, green, yellow, orange, white, purple
- The code has only unique colors, no duplicates.
- Every position must have a color.
- After guessing the Codemaster gives hints.
    - black pin: Correct color and correct position.
    - white pin: Correct color but wrong position.
"""


def mastermind():

    colors = {"r": "Red",
              "b": "Blue",
              "g": "Green",
              "y": "Yellow",
              "o": "Orange",
              "w": "White",
              "p": "Purple"}

    codemaster = random.sample(list(colors.keys()), 4)

    print("Welcome to Mastermind, guess the code!\n")
    for k, v in colors.items():
        print("{}: {}".format(k, v))
    print("\n")

    for tries in range(13):
        try:
            guess = list(input("Your guess: "))
            if not (len(guess) == 4 and set(guess).issubset(set(colors))):  # check if all colors exist
                raise ValueError
        except ValueError:
            print("Invalid input. \n")
            continue
        print("-"*50)
        print("You chose: 1: {}, 2: {}, 3: {}, 4: {}".format(*[colors[c] for c in guess]))

        if guess == codemaster:
            print("You cracked the code! Congratulations!")
            break
        else:
            black_pin = 0
            white_pin = 0
            for color in range(4):
                if guess[color] == codemaster[color]:
                    black_pin += 1
                elif guess[color] in codemaster:
                    white_pin += 1
            print("{} black pins. {} white pins. \n".format(black_pin, white_pin) + "-"*27)

    print("The code was {}.".format("".join(codemaster)))


if __name__ == "__main__":
    mastermind()
    while input("Again? Press \"y\"!").lower().startswith("y"):
        mastermind()
