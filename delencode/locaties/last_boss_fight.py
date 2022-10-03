import keyboard
import time
import random
import os
from colorama import Fore


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


clear = lambda: os.system("cls")
hp = 200
leopard_hp = 400
leopard_total_hp = 400


def last_boss_fight():
    global hp
    global leopard_hp
    global leopard_total_hp

    hp = 200
    leopard_hp = 400
    leopard_total_hp = 400

    print("You reach the top of the mountain. It's snowing very hard.")
    good_key = False
    ran_keys = ["q", "w", "e", "a", "s", "d"]
    print(
        "Info small mini game: You'll see a letter coming up. You need to press this key as fast as possible."
    )
    input("Are you ready? (Press enter)")
    dmg = 0
    leopard_dmg = 0
    while leopard_hp > 0:
        print(
            f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] Press the given letter as fast as possible to do damage!"
        )
        print("")
        print(
            f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] Current equipped loadout: {Fore.MAGENTA}Metal Sword {Fore.WHITE}(10,15) DMG\n"
        )
        print(
            f"[{Fore.GREEN}+{Fore.WHITE}] Snow leopard! hit for {dmg}. Curren health: {healthbar_enemy(leopard_hp, leopard_total_hp)} {Fore.RED}{leopard_hp}{Fore.WHITE}/{leopard_total_hp}"
        )
        print(
            f"[{Fore.RED}-{Fore.WHITE}] You got hit for {leopard_dmg}. Curren health: {healthbar_lategame(hp)} {Fore.GREEN}{hp}{Fore.WHITE}/200\n"
        )
        if hp > 0:
            time.sleep(0.1)
            good_key = False
            ran_key = random.choice(ran_keys)
            print(f"{Fore.WHITE}Key to press: {Fore.YELLOW}" + ran_key)
            start_time = time.time()
            if keyboard.read_key() == ran_key:
                good_key = True
            else:
                good_key = False

            time_key = time.time() - start_time

            leopard_dmg = random.randint(4, 6)
            if good_key and time_key < 1.2:
                dmg = random.randint(10, 15)
            else:
                dmg = 0
            leopard_hp = leopard_hp - dmg
            hp = hp - leopard_dmg
            clear()

        else:
            print("You died!")
            break

    if leopard_hp < 0:
        print("You succesfully beaten the snow leopard!")
    else:
        input("Press enter to try again")
        last_boss_fight()


# time counte hoelang duurt, als dit te lang dan zeggen dat ze zijn gehit...q
last_boss_fight()
