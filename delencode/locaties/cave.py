from colorama import Fore
import time
import random
import os

clear = lambda: os.system('cls')
inventory = ['wood sword']
hp = 100

def healthbar(hp):
    health = hp // 10
    removed_health = (10 - health)
    health_bar = f'|{Fore.GREEN}'

    for i in range(health):
        health_bar += f'x'
    for i in range(removed_health):
        health_bar += f'{Fore.RED}x'

    health_bar += f'{Fore.WHITE}|'
    return health_bar

def healthbar_enemy(enemy_hp, enemy_total_hp):
    health = enemy_hp // 10
    enemy_hp_left = enemy_total_hp // 10
    removed_health = (enemy_hp_left - health)
    health_bar = f'|{Fore.GREEN}'

    for i in range(health):
        health_bar += f'x'
    for i in range(removed_health):
        health_bar += f'{Fore.RED}x'

    health_bar += f'{Fore.WHITE}|'
    return health_bar

def cave():
    global hp
    
    print("You walk towards the cave. It's very dark, but you think you can see some movement.")

    invalid = True
    while invalid:

        decision = input(f'\n[{Fore.YELLOW}!{Fore.WHITE}] Do you want to continue (yes/no): ')

        if decision == 'yes':

            died = False
            invalid = False
            enemy_hp = 133
            enemy_total_hp = 133
            print("\nYou walk in the cave and suddenly three skeletons pop out of nowhere. You'll have to fight.")
            time.sleep(2)
            clear()

            while enemy_hp > 0:

                if hp > 0:
                    if 'wood sword' in inventory:
                        dmg = random.randint(5,10)
                    else:
                        dmg = random.randint(1,3)
                    skeleton_dmg = random.randint(2,4)
                    enemy_hp = enemy_hp - dmg
                    hp = hp - skeleton_dmg

                    print(f'[{Fore.GREEN}+{Fore.WHITE}] Skeletons hit for {dmg}. Curren health: {healthbar_enemy(enemy_hp, enemy_total_hp)} {Fore.RED}{enemy_hp}{Fore.WHITE}/{enemy_total_hp}')
                    print(f'[{Fore.RED}-{Fore.WHITE}] You got hit for {skeleton_dmg}. Curren health: {healthbar(hp)} {Fore.GREEN}{hp}{Fore.WHITE}/100\n')
                    time.sleep(0.4)
                    clear()
                
                else:
                    died = True
                    break

            
            if died:
                print('You died! Maybe you could have prepared yourself better? ')
                time.sleep(3)
                #died()
            else:
                print(f'[{Fore.MAGENTA}!{Fore.WHITE}] One of the skeletons had a wooden shield on him. You grab it. +{Fore.MAGENTA} Wood Shield{Fore.WHITE}!')
                inventory.append('wood shield')
        
        elif decision == 'no':
            invalid = False
            #begin()
        
        else:
            print('Invalid input, try again.')

cave()