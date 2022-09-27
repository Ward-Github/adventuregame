import random
from colorama import Fore
import time

hp = 100
inventory = []

def cave():
    global hp
    
    print("You walk towards the cave. It's very dark, but you think you can see some movement.")

    invalid = True
    while invalid:

        decision = input(f'\n[{Fore.YELLOW}!{Fore.WHITE}]Do you want to continue (yes/no): ')

        if decision == 'yes':

            if 'wood_sword' in inventory:
                hp_skeleton = 133
                print("\nYou walk in the cave and suddenly three skeletons pop out of nowhere. You'll have to fight.")

                while hp_skeleton > 0:

                    wood_sword_dmg = random.randint(5,10)
                    skeleton_dmg = random.randint(2,4)
                    hp_skeleton = hp_skeleton - wood_sword_dmg
                    hp = hp - skeleton_dmg

                    print(f'[{Fore.GREEN}+{Fore.WHITE}] Skeleton hit for {wood_sword_dmg}')
                    time.sleep(0.2)
                    print(f'[{Fore.RED}-{Fore.WHITE}] You got hit for {skeleton_dmg}')

                print(f'\n[{Fore.GREEN}!{Fore.WHITE}] You have succesfully killed the skeletons with {Fore.GREEN}{hp}{Fore.WHITE} health left!')
                print(f'\n[{Fore.GREEN}!{Fore.WHITE}] One of the skeletons had a {Fore.LIGHTMAGENTA_EX}shield{Fore.WHITE} on him. You grab it and put in your bag. +')

                inventory.append('wood_shield')
                invalid = False
            
            else:
                print("You died. You fought hard, but you didn't have any weapons.")
                time.sleep(2)
                #died()
        
        elif decision == 'no':
            invalid = False
            #begin()
        
        else:
            print('Invalid input, try again.')

cave()