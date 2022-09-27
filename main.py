import random
from colorama import Fore, Back, Style

inventory = ['wood_sword']
hp = 100

def died():

    input('Sadly you have not made it to the end. Press enter to try again!')
    begin()

def upper_word_puzzle():

    print("""
You see a note next to it with the following text:

Nothing Good Ever Comes Of Violence.
    """)

    real_code = 'ngecov'

    code = None
    while code != real_code:

        code = input('Code: ')

        if code == real_code:
            print('\nThe chest has opened! You have received a sword')
            inventory.append('wood_sword')
            print('\nYou walk back to the beginning to where you woke up with your brand new sword!')
            begin()

        else:
            print('The code failed. Maybe something different will work? ')

def small_house():

    print("""
You enter a small broken down home. It's very dusty and you can barely see. In the corner u spot an old chest with a lock on it
    """)

    choice = input('Do you want to try to open it or leave the home (open/leave): ')

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

        direction = input("[{Fore.YELLOW}!{Fore.WHITE}] What direction would you like to go (right/left): ")

        if direction ==  'left':
            print("\nYou have chose to follow the path to the cave")
            invalid = False
            cave()

        elif direction == 'right':
            print("\nYou have chosen the path through the woods to the small house.")
            invalid = False
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

            if 'wood_sword' in inventory:
                hp_skeleton = 133
                print("\nYou walk in the cave and suddenly three skeletons pop out of nowhere. You'll have to fight.")

                while hp_skeleton > 0:

                    wood_sword_dmg = random.randint(5,10)
                    skeleton_dmg = random.randint(2,4)
                    hp_skeleton = hp_skeleton - wood_sword_dmg
                    hp = hp - skeleton_dmg

                    print(f'[{Fore.GREEN}+{Fore.WHITE}] Skeleton hit for {wood_sword_dmg}')
                    print(f'[{Fore.RED}-{Fore.WHITE}] You got hit for {skeleton_dmg}')

                print(f'\n[{Fore.GREEN}!{Fore.WHITE}] You have succesfully killed the skeletons with {Fore.GREEN}{hp}{Fore.WHITE} health left!')
                invalid = False
            
            else:
                print("You died. You fought hard, but you didn't have any weapons.")
                died()
        
        elif decision == 'no':
            invalid = False
            begin()
        
        else:
            print('Invalid input, try again.')

print('''
You’ve awakened traveller,
welcome to mountain Karamja. 
This mountain has been terrorized by the Demi-human called Saradomin,
It is your task to free us from his wrath.
    ''')

begin()