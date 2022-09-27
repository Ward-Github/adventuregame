import random

hp = 100

def cave():
    global hp

    print("You walk towards the cave. It's very dark, but you think you can see some movement.")

    invalid = True
    while invalid:

        decision = input('Do you want to continue (yes/no): ')

        if decision == 'yes':

            wood_sword_dmg = random.randint(5,10)
            skeleton_dmg = random.randint(2,4)
            hp_skeleton = 133

            while hp_skeleton > 0:
                hp_skeleton = hp_skeleton - wood_sword_dmg
                hp = hp - skeleton_dmg
            
            print(f'You have succesfully killed the skeletons with {hp} health left!')
            invalid = False
        
        elif decision == 'no':
            invalid = False
            #begin()
        
        else:
            print('Invalid input, try again.')

cave()