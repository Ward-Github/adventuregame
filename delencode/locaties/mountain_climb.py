import random
import time
import os
from colorama import Fore


def tiles_puzzle():
    text = f"""
    In front of you there are 5 lines of tiles. The first row being 1, second 2 etc.
    You will see a combination of numbers for 3 seconds. This is the order to know on what tile to step on.

    |x x x x x|
     1 2 3 4 5

    {Fore.GREEN}Make sure to remember the combination!{Fore.WHITE}

    Make a wrong choice and you will be shot by one of the many traps.
    """

    print(text)

    input(f"[{Fore.YELLOW}!{Fore.WHITE}] Are you ready to start? (Press enter)")

    clear = lambda: os.system("cls")
    numbers = ["1", "2", "3", "4", "5"]
    ran_num = random.choices(numbers, k=5)

    clear()
    print("\n" + "".join(ran_num))

    time.sleep(3)

    clear()
    print(text)

    i = 0
    made_tiles = False
    print("|x x x x x|")
    for i in range(5):
        decision = input("What row to step on (1,2,3,4,5): ")
        if decision == ran_num[i]:
            made_tiles = True
        else:
            made_tiles = False
            break

    if made_tiles:
        print("You succesfully made it to the end.")
    else:
        print("You got shot by an trap! Sadly u died.")
        # died()


def mountain_climb():
    print(
        "You walk towards the the big walls. You see a entrance with very big doors.\nBehind the walls there is a big side of the mountain leiding to the snowy tops.\n"
        "When u reach the entrance the doors automatically open up and you step inside."
    )

    decision = ""
    while decision != "further" and decision != "back":
        decision = input(
            f"\n[{Fore.YELLOW}!{Fore.WHITE}] Do you want to go further or go back (further/back): "
        )
        if decision == "further":
            tiles_puzzle()
        elif decision == "back":
            print("You try to walk back, but the doors instantly closes.")
            tiles_puzzle()
        else:
            print("Invalid input, try again.")


mountain_climb()
