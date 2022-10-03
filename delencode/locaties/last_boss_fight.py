import keyboard
import time
import random
import os

clear = lambda: os.system("cls")


def last_boss_fight():
    """
    print("You reach the top of the mountain. It's snowing very hard.")
    ran_keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while True:  # making a loop
        ran_key = random.choice(ran_keys)
        start_time = time.time()
        print(ran_key)
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed(ran_key):  # if key 'q' is pressed
                print("You Pressed The Right Key!")
                break
        except:
            break  # if user pressed a key other than the given key the loop will break
    print("--- %s seconds ---" % (time.time() - start_time))
    """
    print("You reach the top of the mountain. It's snowing very hard.")
    good_key = False
    ran_keys = ["q", "w", "e", "a", "s", "d"]
    while True:  # making a loop
        ran_key = random.choice(ran_keys)
        print(ran_key)
        start_time = time.time()
        if keyboard.read_key() == ran_key:  # if key 'q' is pressed
            good_key = True
            print(time)
            break  # finishing the loop
        else:
            good_key = False
            break

    time_key = time.time() - start_time

    if good_key:
        print("You pressed the right key!")
        print(time_key)
    else:
        print("Wrong key")
        print(time_key)


# time counte hoelang duurt, als dit te lang dan zeggen dat ze zijn gehit...q
last_boss_fight()
