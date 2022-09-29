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

upper_word_puzzle()