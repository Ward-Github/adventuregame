inventory = []

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
            print('The kist has opened! You have received a sword')
            inventory.append('wood_sword')
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

small_house()
