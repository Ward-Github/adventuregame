import random

def ran_woord_puzzle():
    print("""
    In front of you there is a keypad with a note next to it. On the notepad you see some letters.
    You can probably do something with them to make a working code...
    """)

    words = ['tree','sun','ball','moon','earth','grass','world'] 
    woord = random.choice(words)
    woord_list = list(woord)
    random.shuffle(woord_list)
    final_word = ' '.join(woord_list)
    print(final_word)

    code = None
    while code != woord:
        code = input('Code for the door: ')
        if code == woord:
            print('The door has opened!')
        else:
            print('The code failed. Maybe something different will work? ')

ran_woord_puzzle()
