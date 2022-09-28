from colorama import Fore
import time
import random

inventory = []
hp = 49

def healthbar(hp):
    if hp > 60 and hp <= 80:
        return f'|{Fore.GREEN}xxxx{Fore.RED}-{Fore.WHITE}|'
    elif hp > 80:
        return f'|{Fore.GREEN}xxxxx|'
    elif hp <= 60 and hp > 40:
        return f'|{Fore.GREEN}xxx{Fore.RED}--{Fore.WHITE}|'
    elif hp <= 40 and hp > 20:
        return f'|{Fore.GREEN}xx{Fore.RED}---{Fore.WHITE}|'
    elif hp <= 20 and hp > 0:
        return f'|{Fore.GREEN}x{Fore.RED}----{Fore.WHITE}|'
    elif hp <= 0:
        return f'|{Fore.RED}-----{Fore.WHITE}|'
    


def dragon_fight():
    global hp

    print('You walk the long mountain path. Suddenly you start to hear loud breathing not very far away.')

    dragon_choice = input('Keep walking (yes/no): ')
    invalid = True
    while invalid:
        if dragon_choice == 'yes':
            invalid = False
            dragon_hp = 200
            print("You look around the bush and you see a fire dragon!")
            if 'water_bucket' in inventory:
                print("You think fast and throw your bucket of water on him.")

                dragon_hp = dragon_hp - 100
                print(f"[{Fore.GREEN}+{Fore.WHITE}] -100 HP! His fire went away but he is still moving and angry.")
                print('You grab your sword and shield and start the fight')
            
            else:
                print('You grab your sword and shield and start the fight')

            died = False
            while dragon_hp > 0:

                if hp > 0:
                    wood_sword_dmg = random.randint(10,15)
                    dragon_dmg = random.randint(4,6)
                    dragon_hp = dragon_hp - wood_sword_dmg
                    hp = hp - dragon_dmg

                    print(f'[{Fore.GREEN}+{Fore.WHITE}] Dragon hit for {wood_sword_dmg}. Curren health: {healthbar(hp)} {Fore.RED}{dragon_hp}{Fore.WHITE}/200')
                    time.sleep(0.4)
                    print(f'\n[{Fore.RED}-{Fore.WHITE}] You got hit for {dragon_dmg}. Curren health: {healthbar(hp)} {Fore.GREEN}{hp}{Fore.WHITE}/100\n')
                
                else:
                    died = True
                    break

            if died:
                print('You died! Maybe you could have prepared yourself better? ')
                #died()
            else:
                print(f'\n[{Fore.GREEN}!{Fore.WHITE}] You have succesfully killed the dragon with {Fore.GREEN}{hp}{Fore.WHITE}/100 health left!')

        elif dragon_choice == 'no':
            print('You walk back...')
            break
            #outside_cave()


dragon_fight()