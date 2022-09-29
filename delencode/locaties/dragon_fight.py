from colorama import Fore
import time
import random
import os

clear = lambda: os.system('cls')
inventory = ['water bucket']
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

    
def dragon_fight():
    global hp

    print('You walk the long mountain path. Suddenly you start to hear loud breathing not very far away.')

    dragon_choice = input('Keep walking (yes/no): ')
    invalid = True
    while invalid:
        if dragon_choice == 'yes':
            invalid = False
            enemy_hp = 200
            enemy_total_hp = 200
            print("You look around the bush and you see a fire dragon!")
            if 'water bucket' in inventory:
                print("You think fast and throw your bucket of water on him.")

                enemy_hp = enemy_hp - 100
                print(f"[{Fore.GREEN}+{Fore.WHITE}] -100 HP! His fire went away but he is still moving and angry.")
                print('You grab your sword and shield and start the fight')
            
            else:
                print('You grab your sword and shield and start the fight')

            died = False
            while enemy_hp > 0:

                if hp > 0:
                    wood_sword_dmg = random.randint(10,15)
                    dragon_dmg = random.randint(4,6)
                    enemy_hp = enemy_hp - wood_sword_dmg
                    hp = hp - dragon_dmg

                    print(f'[{Fore.GREEN}+{Fore.WHITE}] Dragon hit for {wood_sword_dmg}. Curren health: {healthbar_enemy(enemy_hp, enemy_total_hp)} {Fore.RED}{enemy_hp}{Fore.WHITE}/{enemy_total_hp}')
                    print(f'[{Fore.RED}-{Fore.WHITE}] You got hit for {dragon_dmg}. Curren health: {healthbar(hp)} {Fore.GREEN}{hp}{Fore.WHITE}/100\n')
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
                print(f'\n[{Fore.GREEN}!{Fore.WHITE}] You have succesfully killed the dragon with {Fore.GREEN}{hp}{Fore.WHITE}/100 health left!')

        elif dragon_choice == 'no':
            print('You walk back...')
            break
            #outside_cave()


dragon_fight()