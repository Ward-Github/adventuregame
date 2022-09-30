import random
from colorama import Fore
import os
import time

inventory = ['wood sword', 'water bucket']
hp = 100
clear = lambda: os.system('cls')

def died():
    clear()
    input('Thank you for playing our game! Sadly you have not made it to the end. Press enter to try again! ')
    begin()

def upper_word_puzzle():

    print("""
You see a note next to it with the following text:

Nothing Good Ever Comes Of Violence.
    """)

    real_code = 'ngecov'

    code = None
    while code != real_code:

        code = input('Code: ').lower()

        if code == real_code:
            clear()
            print('\nThe chest has opened! You have received a sword')
            inventory.append('wood_sword')
            print(f'\nYou walk back to the beginning to where you woke up with your brand new {Fore.LIGHTMAGENTA_EX}sword{Fore.WHITE}!')
            begin()

        else:
            print('The code failed. Maybe it has something to do with the beggining of each word? ')

def small_house():

    print("""
You enter a small broken down home. It's very dusty and you can barely see. In the corner u spot an old chest with a lock on it
    """)

    choice = input(f'[{Fore.YELLOW}!{Fore.WHITE}] Do you want to try to open it or leave the home (open/leave): ')

    if choice == 'open':
        upper_word_puzzle()
    
    else:
        print('Leaved huis')

def begin():

    print("""
On your right side there is a small house, Follow the path through the woods and you will find it.
On your left side there is a cave, Follow the path over the bridge to the cave.
    """)

    invalid = True
    while invalid:

        direction = input(f"[{Fore.YELLOW}!{Fore.WHITE}] What direction would you like to go (right/left): ")

        if direction ==  'left':
            print("\nYou have chose to follow the path to the cave")
            invalid = False
            clear()
            cave()

        elif direction == 'right':
            print("\nYou have chosen the path through the woods to the small house.")
            invalid = False
            clear()
            small_house()

        else:
            print("invalid choice.")

def cave():
    global hp
    
    print("You walk towards the cave. It's very dark, but you think you can see some movement.")

    invalid = True
    while invalid:

        decision = input(f'\n[{Fore.YELLOW}!{Fore.WHITE}]Do you want to continue (yes/no): ')

        if decision == 'yes':

            if 'wood sword' in inventory:
                enemy_hp = 133
                print("\nYou walk in the cave and suddenly three skeletons pop out of nowhere. You'll have to fight.")

                while enemy_hp > 0:

                    wood_sword_dmg = random.randint(5,10)
                    skeleton_dmg = random.randint(2,4)
                    enemy_hp = enemy_hp - wood_sword_dmg
                    hp = hp - skeleton_dmg

                    print(f'[{Fore.GREEN}+{Fore.WHITE}] Skeleton hit for {wood_sword_dmg}')
                    time.sleep(0.2)
                    print(f'[{Fore.RED}-{Fore.WHITE}] You got hit for {skeleton_dmg}')

                print(f'\n[{Fore.GREEN}!{Fore.WHITE}] You have succesfully killed the skeletons with {Fore.GREEN}{hp}{Fore.WHITE} health left!')
                time.sleep(0.2)
                print(f'\n[{Fore.GREEN}!{Fore.WHITE}] One of the skeletons had a {Fore.LIGHTMAGENTA_EX}shield{Fore.WHITE} on him. You grab it and put in your bag. ')
                time.sleep(1)
                invalid = False
                outside_cave()
            
            else:
                print("You died. You fought hard, but you didn't have any weapons.")
                time.sleep(2)
                died()
        
        elif decision == 'no':
            invalid = False
            begin()
        
        else:
            print('Invalid input, try again.')

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
            dragon_fight()

        elif decision == 'left':
            invalid = False
            #giant_fight()
        
        elif decision == 'ahead':
            print('Ff zodat geen error')
            #water_well()
        
        else:
            print('Invalid input, try again')

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

                    print(f'[{Fore.GREEN}+{Fore.WHITE}] Dragon hit for {wood_sword_dmg}. Curren health: {healthbar_enemy(enemy_hp, enemy_total_hp)} {Fore.RED}{enemy_hp}{Fore.WHITE}/200')
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

print(f"""

  ██████  ▄▄▄       ██▀███   ▄▄▄      ▓█████▄  ▒█████   ███▄ ▄███▓ ██▓ ███▄    █ 
▒██    ▒ ▒████▄    ▓██ ▒ ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ 
░ ▓██▄   ▒██  ▀█▄  ▓██ ░▄█ ▒▒██  ▀█▄  ░██   █▌▒██░  ██▒▓██    ▓██░▒██▒▓██  ▀█ ██▒
  ▒   ██▒░██▄▄▄▄██ ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░▒██    ▒██ ░██░▓██▒  ▐▌██▒
▒██████▒▒ ▓█   ▓██▒░██▓ ▒██▒ ▓█   ▓██▒░▒████▓ ░ ████▓▒░▒██▒   ░██▒░██░▒██░   ▓██░
▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ 
░ ░▒  ░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░ ░  ░      ░ ▒ ░░ ░░   ░ ▒░
░  ░  ░    ░   ▒     ░░   ░   ░   ▒    ░ ░  ░ ░ ░ ░ ▒  ░      ░    ▒ ░   ░   ░ ░ 
      ░        ░  ░   ░           ░  ░   ░        ░ ░         ░    ░           ░ 
                                       ░                                         

[{Fore.YELLOW}!{Fore.WHITE}] Welcome to Saradomin

""")
input(f"[{Fore.YELLOW}/{Fore.WHITE}] Press enter to start... (If you can't see colors make sure to update your terminal")

clear()

print('''
You’ve awakened traveller,
welcome to mountain Karamja. 
This mountain has been terrorized by the Demi-human called Saradomin,
It is your task to free us from his wrath.''')

begin()