from colorama import Fore
import time

inventory = []
hp = 100

def outside_cave():
    global hp

    print("""
You finally made it out of the cave, thinking about what to do next.

On your left you see a giant person. Higher than the biggest tree.
On your right you see a regular mountain path.
In front of you you see water well.
    """)

    decision = input(f'[{Fore.YELLOW}!{Fore.WHITE}] Where do you want to go (right/left/ahead): ')

    if decision == 'right':
        print('You walk the long mountain path. Suddenly you start to hear loud breathing not very far away.')
        dragon_choice = input('Keep walking (yes/no): ')
        if dragon_choice == 'yes':
            dragon_hp = 200
            if 'water_bucket' in inventory:
                print("You look around the bush and you see a fire dragon!")
                print("You think fast and throw your bucket of water on him.")

                dragon_hp = dragon_hp - 100
                print("His fire went away but he is still moving and angry.")

    elif decision == 'left':
        print('You walk towards the gaint')
        for i in range(3):
            print('...')
            time.sleep(0.6)
        print('He raises his leg and squishes you.')
        #died()

outside_cave()