
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
while True:
    Fate = input("Do you wish to continue? Yes/No")
    if Fate == 'No':
        print("There is no returning back once you started, You have died.")
    elif Fate == 'Yes':
        print("""Very well, To learn the name of the correct wall you must solve this clue.
    This answer to this clue is the name of the correct wall, and will guide you to the right direction.
""")
    else:
        print("Should have answered with yes or no, fool. You have died.")
    break

Answer = input("What is made of water, but when placed in water it will die?")
if Answer == 'Snow':
    print("Congratulations traveller, you are smart enough to continue on ur path. Best of luck.")
elif Answer == 'Grass':
    print("Unfortunately you are clearly not cut out for this. Im sorry but we must diminish ur existence.")
elif Answer == 'Sand':
    print("Unfortunately you are clearly not cut out for this. Im sorry but we must diminish ur existence.")
elif Answer == 'Fog':
    print("Unfortunately you are clearly not cut out for this. Im sorry but we must diminish ur existence.")


