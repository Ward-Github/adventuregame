
def lever_riddle():
    print(''' Welcome traveller. 
To continue on this path you have to choose the wall with the correct lever.
Each wall has its own name.
Snow
Grass
Sand
Fog
If you choose the incorrect lever you will be met with the fate of death.
If you choose the correct lever you will be allowed to continue.
    ''')

    fate = input("Do you wish to continue? Yes/No")
    if fate == 'No':
        print("There is no returning back once you started, You have died.")
        #died()
    elif fate == 'Yes':
        print("""Very well, To learn the name of the correct wall you must solve this clue.
    This answer to this clue is the name of the correct wall, and will guide you to the right direction.
    """)
    else:
        print("Should have answered with yes or no, fool. You have died.")
        #died()

    answer = input("What is made of water, but when placed in water it will die?")
    if answer == 'Snow':
        print("Congratulations traveller, you are smart enough to continue on ur path. Best of luck.")
    elif answer == 'Grass':
        print("Unfortunately you are clearly not cut out for this. Im sorry but we must diminish ur existence.")
        #died()
    elif answer == 'Sand':
        print("Unfortunately you are clearly not cut out for this. Im sorry but we must diminish ur existence.")
        #died()
    elif answer == 'Fog':
        print("Unfortunately you are clearly not cut out for this. Im sorry but we must diminish ur existence.")
        #died()

lever_riddle()





