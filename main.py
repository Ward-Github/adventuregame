import random
from colorama import Fore
import os
import time


inventory = ["wood sword"]
hp = 100
clear = lambda: os.system("cls")


def healthbar_lategame(hp):
    health = hp // 10
    removed_health = 20 - health
    health_bar = f"|{Fore.GREEN}"

    for i in range(health):
        health_bar += f"x"
    for i in range(removed_health):
        health_bar += f"{Fore.RED}x"

    health_bar += f"{Fore.WHITE}|"
    return health_bar


def inventory_show():
    print("Inventory:")
    for i in range((len(inventory))):
        print(inventory[i])


def died():
    clear()
    input(
        "Thank you for playing our game! Sadly you have not made it to the end. Press enter to try again! "
    )
    begin()


def upper_word_puzzle():

    print(
        """
You see a note next to it with the following text:

Nothing Good Ever Comes Of Violence.
    """
    )

    real_code = "ngecov"

    code = None
    while code != real_code:

        code = input("Code: ").lower()

        if code == real_code:
            clear()
            print("\nThe chest has opened! You have received a sword")
            inventory.append("wood sword")
            print(
                f"\nYou walk back to the beginning to where you woke up with your brand new {Fore.LIGHTMAGENTA_EX}sword{Fore.WHITE}!"
            )
            begin()

        else:
            print(
                "The code failed. Maybe it has something to do with the beggining of each word? "
            )


def small_house():

    print(
        """
You enter a small broken down home. It's very dusty and you can barely see. In the corner u spot an old chest with a lock on it
    """
    )

    choice = input(
        f"[{Fore.YELLOW}!{Fore.WHITE}] Do you want to try to open it or leave the home (open/leave): "
    )

    if choice == "open":
        upper_word_puzzle()

    else:
        print("Leaved huis")


def begin():

    print(
        """
On your right side there is a small house, Follow the path through the woods and you will find it.
On your left side there is a cave, Follow the path over the bridge to the cave.
    """
    )

    invalid = True
    while invalid:

        direction = input(
            f"[{Fore.YELLOW}!{Fore.WHITE}] What direction would you like to go (right/left): "
        )

        if direction == "left":
            print("\nYou have chose to follow the path to the cave")
            invalid = False
            clear()
            cave()

        elif direction == "right":
            print("\nYou have chosen the path through the woods to the small house.")
            invalid = False
            clear()
            small_house()

        else:
            print("invalid choice.")


def cave():
    global hp
    global inventory

    print(
        "You walk towards the cave. It's very dark, but you think you can see some movement."
    )

    invalid = True
    while invalid:

        decision = input(
            f"\n[{Fore.YELLOW}!{Fore.WHITE}] Do you want to continue (yes/no): "
        )

        if decision == "yes":

            died = False
            invalid = False
            enemy_hp = 133
            enemy_total_hp = 133
            print(
                "\nYou walk in the cave and suddenly three skeletons pop out of nowhere. You'll have to fight."
            )
            time.sleep(2)
            clear()

            while enemy_hp > 0:

                if hp > 0:
                    if "wood sword" in inventory:
                        dmg = random.randint(5, 10)
                    else:
                        dmg = random.randint(1, 3)
                    skeleton_dmg = random.randint(2, 4)
                    enemy_hp = enemy_hp - dmg
                    hp = hp - skeleton_dmg

                    print(
                        f"[{Fore.MAGENTA}!{Fore.WHITE}] Current equipped loadout: {Fore.MAGENTA}Wooden Sword {Fore.WHITE}(5,10) DMG\n"
                    )
                    print(
                        f"[{Fore.GREEN}+{Fore.WHITE}] Skeletons hit for {dmg}. Curren health: {healthbar_enemy(enemy_hp, enemy_total_hp)} {Fore.RED}{enemy_hp}{Fore.WHITE}/{enemy_total_hp}"
                    )
                    print(
                        f"[{Fore.RED}-{Fore.WHITE}] You got hit for {skeleton_dmg}. Curren health: {healthbar(hp)} {Fore.GREEN}{hp}{Fore.WHITE}/100\n"
                    )
                    time.sleep(0.4)
                    clear()

                else:
                    died = True
                    break

            if died:
                print("You died! Maybe you could have prepared yourself better? ")
                print(inventory)
                time.sleep(3)
                died()
            else:
                print(
                    f"[{Fore.MAGENTA}!{Fore.WHITE}] One of the skeletons had a wooden shield on him. You grab it. +{Fore.MAGENTA} Wood Shield{Fore.WHITE}!"
                )
                inventory.append("wood shield")
                outside_cave()

        elif decision == "no":
            invalid = False
            begin()

        else:
            print("Invalid input, try again.")


def outside_cave():

    print(
        """
On your left you see a giant person. Higher than the biggest tree.
On your right you see a regular mountain path.
In front of you you see water well.
    """
    )

    invalid = True
    while invalid:
        decision = input(
            f"[{Fore.YELLOW}!{Fore.WHITE}] Where do you want to go (right/left/ahead): "
        )
        if decision == "right":
            invalid = False
            dragon_fight()

        elif decision == "left":
            invalid = False
            giant_fight()

        elif decision == "ahead":
            print("Ff zodat geen error")
            # water_well()

        else:
            print("Invalid input, try again")


def healthbar(hp):
    health = hp // 10
    removed_health = 10 - health
    health_bar = f"|{Fore.GREEN}"

    for i in range(health):
        health_bar += f"x"
    for i in range(removed_health):
        health_bar += f"{Fore.RED}x"

    health_bar += f"{Fore.WHITE}|"
    return health_bar


def healthbar_enemy(enemy_hp, enemy_total_hp):
    health = enemy_hp // 10
    enemy_hp_left = enemy_total_hp // 10
    removed_health = enemy_hp_left - health
    health_bar = f"|{Fore.GREEN}"

    for i in range(health):
        health_bar += f"x"
    for i in range(removed_health):
        health_bar += f"{Fore.RED}x"

    health_bar += f"{Fore.WHITE}|"
    return health_bar


def dragon_fight():
    global hp

    print(
        "You walk the long mountain path. Suddenly you start to hear loud breathing not very far away."
    )

    dragon_choice = input("Keep walking (yes/no): ")
    invalid = True
    while invalid:
        if dragon_choice == "yes":
            invalid = False
            enemy_hp = 200
            enemy_total_hp = 200
            print("You look around the bush and you see a fire dragon!")
            if "water bucket" in inventory:
                print("You think fast and throw your bucket of water on him.")

                enemy_hp = enemy_hp - 100
                print(
                    f"[{Fore.GREEN}+{Fore.WHITE}] -100 HP! His fire went away but he is still moving and angry."
                )
                print("You grab your sword and shield and start the fight")
                time.sleep(3)

            else:
                print("You grab your sword and shield and start the fight")
                time.sleep(3)

            dead = False
            while enemy_hp > 0:

                if hp > 0:
                    wood_sword_dmg = random.randint(8, 13)
                    dragon_dmg = random.randint(3, 5)
                    enemy_hp = enemy_hp - wood_sword_dmg
                    hp = hp - dragon_dmg

                    print(
                        f"[{Fore.GREEN}+{Fore.WHITE}] Dragon hit for {wood_sword_dmg}. Curren health: {healthbar_enemy(enemy_hp, enemy_total_hp)} {Fore.RED}{enemy_hp}{Fore.WHITE}/200"
                    )
                    print(
                        f"[{Fore.RED}-{Fore.WHITE}] You got hit for {dragon_dmg}. Curren health: {healthbar(hp)} {Fore.GREEN}{hp}{Fore.WHITE}/100\n"
                    )
                    time.sleep(0.4)
                    clear()

                else:
                    dead = True
                    break

            if dead:
                print("You died! Maybe you could have prepared yourself better? ")
                time.sleep(3)
                died()
            else:
                print(
                    f"\n[{Fore.GREEN}!{Fore.WHITE}] You have succesfully killed the dragon with {Fore.GREEN}{hp}{Fore.WHITE}/100 health left!"
                )
                print("")
                print(
                    f"You look around and you see a dead body. You walk up to it and spot some climbing gear. + {Fore.MAGENTA}Climbing gear{Fore.WHITE}"
                )
                print(f"You decide to walk back...")
                time.sleep(1)
                inventory.append("climbing gear")
                outside_cave()

        elif dragon_choice == "no":
            print("You walk back...")
            invalid = False
            outside_cave()

        else:
            print("Invalid input, try again!")


def giant_location():
    print(
        """
On your left you see a cliff
Up ahead you see a wooden house
    """
    )

    decision = ""
    while decision != "left" and decision != "ahead":
        decision = input("Where would you like to go (left/ahead): ")
        if decision == "left":
            print("ff geen error")
            cliff()
        elif decision == "ahead":
            print("ff geen error")
            mountain_climb()
        else:
            print("Invalid input, try again!")


def giant_fight():
    global giant_hp
    global giant_total_hp
    global hp
    global giant_beaten

    print(
        """
You think about what to do next...

1. Use item on him
2. Fight him
3. Try to sneak past him
4. Look around
5. Go back
    """
    )
    decision = ""
    # Bij deze keuzes moet hij niet opnieuw vragen.
    while decision != "1" and decision != "2" and decision != "3" and decision != "5":
        decision = input("What to do (1/2/3/4): ")

        if decision == "1":
            giant_itemmenu()
        elif decision == "2":

            died = False
            print("\nYou walk up a cliff so that you around waist height of the giant.")
            print("He notices you and the fight begins")
            time.sleep(2)
            clear()

            while giant_hp > 0:

                if hp > 0:

                    # 10 procent kans dat hij de aanval blockt
                    blocked = False
                    if random.randint(0, 100) < 10:
                        blocked = True
                    else:
                        blocked = False

                    if "metal sword" in inventory:
                        dmg = random.randint(10, 15)
                    else:
                        dmg = random.randint(5, 10)
                        giant_dmg = random.randint(4, 6)

                    if blocked:
                        giant_hp = giant_hp - dmg
                        print(
                            f"[{Fore.GREEN}+{Fore.WHITE}] Giant hit for {dmg}. Curren health: {healthbar_enemy(giant_hp, giant_total_hp)} {Fore.RED}{giant_hp}{Fore.WHITE}/{giant_total_hp}"
                        )
                        print(
                            f"[{Fore.RED}-{Fore.WHITE}] You {Fore.GREEN}blocked{Fore.WHITE} the attack with your shield! Curren health: {healthbar_lategame(hp)} {Fore.GREEN}{hp}{Fore.WHITE}/200\n"
                        )
                        time.sleep(0.4)
                        clear()

                    else:
                        giant_hp = giant_hp - dmg
                        hp = hp - giant_dmg

                        print(
                            f"[{Fore.GREEN}+{Fore.WHITE}] Giant hit for {dmg}. Curren health: {healthbar_enemy(giant_hp, giant_total_hp)} {Fore.RED}{giant_hp}{Fore.WHITE}/{giant_total_hp}"
                        )
                        print(
                            f"[{Fore.RED}-{Fore.WHITE}] You got hit for {giant_dmg}. Curren health: {healthbar_lategame(hp)} {Fore.GREEN}{hp}{Fore.WHITE}/200\n"
                        )
                        time.sleep(0.4)
                        clear()

                else:
                    died = True
                    break

            if died:
                print("You died! Maybe you could have prepared yourself better? ")
                time.sleep(3)
                # died()
            else:
                print("After a long fight the giant is finally dead.\n")
                print("You see ")

        elif decision == "3":
            for i in range(3):
                print("...")
                time.sleep(0.4)
            print("He steps on you with full force.")
            time.sleep(3)
            died()

        elif decision == "4":
            print(
                "You decide to look around the area. You notice something reflecting the sun light."
            )
            print(
                f"You walk close and its a metal sword! + {Fore.MAGENTA}metal sword{Fore.WHITE}"
            )
            inventory.append("metal sword")

        elif decision == "5":
            stop = True
            outside_cave()

        else:
            print("Invalid input, try again")


def giant_itemmenu():
    global giant_hp
    global giant_total_hp
    inventory_show()
    valid = False
    print(f"To return to choices type {Fore.YELLOW}menu{Fore.WHITE}")
    while not valid:
        item_use = input("\nWhat item to use (ex. wooden shield): ")

        if item_use == "wooden shield":
            print("You already have this item equipped. ")

        elif item_use == "wooden sword":
            print("You already have this item equipped. ")

        elif item_use == "climbing gear":
            print(
                "You sneak up on the giant and start climbing on him.\nOnce you reach his head you grab your sword and stab both of his eyes"
            )
            print(
                "He falls down in pain. You slide down his head and go back hiding in the bush"
            )
            print(f"{Fore.RED}-200{Fore.WHITE} HP of the Giant!")
            giant_hp = giant_hp - 200
            giant_total_hp = giant_total_hp - 200

        elif item_use == "water_bucket":
            print("You try to throw water on him.")
            for i in range(3):
                print(...)
                time.sleep(0.4)
            print("He steps on you with full force.")
            time.sleep(3)
            died()

        elif item_use == "menu":
            valid = True
            giant_fight()

        else:
            print("This is not a valid option...")


def tiles_puzzle():
    text = f"""
    In front of you there are 5 lines of tiles. The first row being 1, second 2 etc.
    You will see a combination of numbers for 3 seconds. This is the order to know on what tile to step on.

    |x x x x x|
     1 2 3 4 5

    {Fore.GREEN}Make sure to remember the combination!{Fore.WHITE}

    Make a wrong choice and you will be shot by one of the many traps.
    """

    print(text)

    input(f"[{Fore.YELLOW}!{Fore.WHITE}] Are you ready to start? (Press enter)")

    clear = lambda: os.system("cls")
    numbers = ["1", "2", "3", "4", "5"]
    ran_num = random.choices(numbers, k=5)

    clear()
    print("\n" + "".join(ran_num))

    time.sleep(3)

    clear()
    print(text)

    i = 0
    made_tiles = False
    print("|x x x x x|")
    for i in range(5):
        decision = input("What row to step on (1,2,3,4,5): ")
        if decision == ran_num[i]:
            made_tiles = True
        else:
            made_tiles = False
            break

    if made_tiles:
        print("You succesfully made it to the end.")
    else:
        print("You got shot by an trap! Sadly u died.")
        # died()


def mountain_climb():
    print(
        "You walk towards the the big walls. You see a entrance with very big doors.\nBehind the walls there is a big side of the mountain leiding to the snowy tops.\n"
        "When u reach the entrance the doors automatically open up and you step inside."
    )

    decision = ""
    while decision != "further" and decision != "back":
        decision = input(
            f"\n[{Fore.YELLOW}!{Fore.WHITE}] Do you want to go further or go back (further/back): "
        )
        if decision == "further":
            tiles_puzzle()
        elif decision == "back":
            print("You try to walk back, but the doors instantly closes.")
            tiles_puzzle()
        else:
            print("Invalid input, try again.")


def cliff():
    print("Up ahead you see a cliff with a beautifull view of the forest down below.")
    time.sleep(1)
    print("You look to your right and spot some armor laying on the ground.")
    time.sleep(1)
    print(
        f"You decide to try it on and it fits perfectly! + {Fore.MAGENTA}armor{Fore.WHITE}!"
    )
    inventory.append["armor"]
    print("There is not anything else to do here, so you walk back...")
    time.sleep(2)
    giant_location()


print(
    f"""

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

"""
)
input(
    f"[{Fore.YELLOW}/{Fore.WHITE}] Press enter to start... (If you can't see colors make sure to update your terminal"
)

clear()

print(
    """
You’ve awakened traveller,
welcome to mountain Karamja. 
This mountain has been terrorized by the Demi-human called Saradomin,
It is your task to free us from his wrath."""
)

if __name__ == "__main__":
    begin()
