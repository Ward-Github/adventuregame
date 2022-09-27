
def died():
    input('Sadly you have not made it to the end. Press enter to try again!')
    begin()

def begin():
    
    print('''
You’ve awakened traveller,
welcome to mountain Karamja. 
This mountain has been terrorized by the Demi-human called Saradomin,
It is your task to free us from his wrath.
On your left side there is a small house, Follow the path through the woods and you will find it.
On your right side there is a cave, Follow the path over the bridge to the cave.
    ''')

    direction = input("What direction would you like to go (right/left): ")

    if direction ==  'right':
        print("You have chose to follow the path to the cave")
    elif direction == 'left':
        print("You have chosen the path through the woods to the small house.")
    else:
        print("invalid choice.")

