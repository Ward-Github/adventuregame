import time
from colorama import Fore

inventory = []


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
    # giant_location()
