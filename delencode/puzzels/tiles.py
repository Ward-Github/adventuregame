import random
import time
import os


def tiles_puzzle():
    text = """
    In front of you there are 5 lines of tiles. The first row being 1, second 2 and the thirth is 3.
    You will see a combination of numbers for 3 seconds. This is the order to know on what tile to step on.
    Make a wrong choice and you will be shot by one of the many traps.

    """
    success = "That is right!"
    fail = "You got shot by an trap! Sadly u died."

    print(text)

    input("Are you ready to start? (Press enter)")

    clear = lambda: os.system("cls")
    numbers = ["1", "2", "3", "4", "5"]
    ran_num = random.choices(numbers, k=6)

    print(ran_num)

    time.sleep(3)
    clear()

    print(text)

    i = 0

    for i in range(6):
        decision = input("What row to step on (1,2,3,4,5): ")
        if decision == ran_num[i]:
            print(success)
        else:
            print(fail)
            break
        print("You succesfully made it to the end.")


tiles_puzzle()
