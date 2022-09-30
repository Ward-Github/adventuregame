import os

clear = lambda: os.system("cls")


def died():
    clear()
    input(
        "Thank you for playing our game! Sadly you have not made it to the end. Press enter to try again! "
    )


def lever_riddle():
    print(
        """ Welcome traveller. 
To continue on this path you have to choose the wall with the correct lever.
Each wall has its own name.
Snow
Grass
Sand
Fog
If you choose the incorrect lever you will be met with the fate of death.
If you choose the correct lever you will be allowed to continue.
    """
    )

    fate = input("Do you wish to continue (yes/no): ")
    if fate == "no":
        print("There is no returning back once you started, You have died.")
        died()
    elif fate == "yes":
        print(
            """Very well, To learn the name of the correct wall you must solve this clue.
    This answer to this clue is the name of the correct wall, and will guide you to the right direction.
    """
        )
    else:
        print("Should have answered with yes or no, fool. You have died.")
        died()

    answer = input(
        "What is made of water, but when placed in water it will die (snow/grass/sand/fog):"
    )
    if answer == "snow":
        print(
            "Congratulations traveller, you are smart enough to continue on ur path. Best of luck."
        )
    elif answer == "grass":
        print(
            "Unfortunately you are clearly not cut out for this. Im sorry but we must diminish ur existence."
        )
        died()
    elif answer == "sand":
        print(
            "Unfortunately you are clearly not cut out for this. Im sorry but we must diminish ur existence."
        )
        died()
    elif answer == "fog":
        print(
            "Unfortunately you are clearly not cut out for this. Im sorry but we must diminish ur existence."
        )
        died()


lever_riddle()
