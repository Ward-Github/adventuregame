from colorama import Fore
import time
import random
import os

clear = lambda: os.system("cls")
inventory = ["wooden shield", "wooden sword", "climbing gear", "water bucket"]
giant_hp = 500
giant_total_hp = 500
hp = 200
giant_beaten = False


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


def inventory_show():
    print("Inventory:")
    for i in range((len(inventory))):
        print(inventory[i])


def giant_location():
    print(
        """
On your left you see a cliff
Up ahead you see very big walls. Behind it you see a very big mountain side leading to the snowy tops.
    """
    )

    decision = ""
    while decision != "left" and decision != "ahead":
        decision = input("Where would you like to go (left/ahead): ")
        if decision == "left":
            print("ff geen error")
            # cliff()
        elif decision == "ahead":
            print("ff geen error")
            # mountain_climb()
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
            # died()

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
            # begin()

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
            # died()

        elif item_use == "menu":
            valid = True
            giant_fight()

        else:
            print("This is not a valid option...")


giant_fight()

# Wil gebruikers de keuze laten maken tussen stone sword of hun climbing gear gebruiken. Als zij deze allebei niet hebben moeten ze falen.
