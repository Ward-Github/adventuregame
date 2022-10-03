# guess if dice will be higher or lower
import random


def ran_dice():
    print(
        "The point of this game is that you have to guess if the dice will be higher or lower. So (1,2,3) or (4,5,6)"
    )
    print(
        "You have 3 attempts. If you fail all attempts you will get the healing potion."
    )
    guessed = False
    while not guessed:
        ran_number = random.randint(1, 6)
        choice = int(input("Guess higher or lower (higher/lower): "))
        if ran_number > 3 and choice == "higher":
            print("You guessed it!")
            guessed = True
        elif ran_number < 4 and choice == "lower":
            print("You guessed it!")
            guessed = True
        else:
            print("You failed try again.")
