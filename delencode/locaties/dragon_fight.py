from colorama import Fore
import time
import random
import os

clear = lambda: os.system("cls")
inventory = ["water bucket"]
hp = 100


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


def ran_dice():
    global hp
    print(
        "\nThe point of this game is that you have to guess if the dice will be higher or lower. So (1,2,3) or (4,5,6)"
    )
    print(
        "You have 3 attempts. If you fail all attempts you will get the healing potion."
    )
    guessed = False
    while not guessed:
        ran_number = random.randint(1, 6)
        choice = int(input("Guess higher or lower (higher/lower): "))
        if ran_number > 3 and choice == "higher":
            print("You guessed it!")
            guessed = True
            print(
                f"Your health gets completely restored + boosted. {Fore.GREEN}200{Fore.WHITE}/200 HP"
            )
            hp = 200
        elif ran_number < 4 and choice == "lower":
            print("You guessed it!")
            guessed = True
            print(
                f"Your health gets completely restored + boosted. {Fore.GREEN}200{Fore.WHITE}/200 HP"
            )
            hp = 200
        else:
            print("You failed try again.")


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
                    f"\n[{Fore.GREEN}+{Fore.WHITE}] {Fore.RED}-100{Fore.WHITE} HP! His fire went away but he is still moving and angry."
                )
                print("You grab your sword and shield and start the fight")
                time.sleep(6)

            else:
                print("You grab your sword and shield and start the fight")

            died = False
            while enemy_hp > 0:

                if hp > 0:
                    wood_sword_dmg = random.randint(8, 13)
                    dragon_dmg = random.randint(3, 5)
                    enemy_hp = enemy_hp - wood_sword_dmg
                    hp = hp - dragon_dmg

                    print(
                        f"[{Fore.GREEN}+{Fore.WHITE}] Dragon hit for {wood_sword_dmg}. Curren health: {healthbar_enemy(enemy_hp, enemy_total_hp)} {Fore.RED}{enemy_hp}{Fore.WHITE}/{enemy_total_hp}"
                    )
                    print(
                        f"[{Fore.RED}-{Fore.WHITE}] You got hit for {dragon_dmg}. Curren health: {healthbar(hp)} {Fore.GREEN}{hp}{Fore.WHITE}/100\n"
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
                print(
                    f"\n[{Fore.GREEN}!{Fore.WHITE}] You have succesfully killed the dragon with {Fore.GREEN}{hp}{Fore.WHITE}/100 health left!"
                )
                print("")
                time.sleep(1)
                print(
                    f"You look around and you see a dead body. You walk up to it and spot some climbing gear. + {Fore.MAGENTA}Climbing gear{Fore.WHITE}"
                )
                time.sleep(1)
                inventory.append("climbing gear")
                print("You walk back...")
                for i in range(3):
                    print("...")
                    time.sleep(0.4)
                print(
                    "You notice somebody with a large backpack standing on the path. You walk up to him and start a conversation"
                )
                time.sleep(2)
                print("\nYou find out he is also lost on this mountain.")
                print(
                    f"He challenges you to a simple game in order to get a {Fore.MAGENTA}healing spell{Fore.WHITE}!"
                )
                ran_dice()
                time.sleep(2)
                print(
                    f"Your health gets completely restored + boosted. {Fore.GREEN}200{Fore.WHITE}/200 HP"
                )
                hp = 200
                # outside_cave()

        elif dragon_choice == "no":
            print("You walk back...")
            break
            # outside_cave()


dragon_fight()
