from colorama import Fore

def outside_cave():

    print("""
You finally made it out of the cave, thinking about what to do next.

On your left you see a giant person. Higher than the biggest tree.
On your right you see a regular mountain path.
In front of you you see water well.
    """)

    invalid = True
    while invalid:
        decision = input(f'[{Fore.YELLOW}!{Fore.WHITE}] Where do you want to go (right/left/ahead): ')
        if decision == 'right':
            invalid = False
            #dragon_fight()

        elif decision == 'left':
            invalid = False
            #giant_fight()
        
        elif decision == 'ahead':
            print('Ff zodat geen error')
            #water_well()
        
        else:
            print('Invalid input, try again')

outside_cave()