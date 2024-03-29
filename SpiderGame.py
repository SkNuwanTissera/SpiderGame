from random import randint


# need to show the progress of the spider through the game and add different players
def replacer(index, character, array):
    array.pop(index)
    array.insert(index, character)
    return array


def game():
    drawnSpider = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
    temp = []
    score = 0
    body = 0
    leg = 0
    eye = 0
    runner = 'y'
    while runner == 'y':
        die = randint(1, 6)
        score += 1
        print("Turn", score)
        print("You rolled a ", die, "\n")

# Printing the body
        if die == 2 or die == 5:
            print("Not a valid throw ", "\n")

        if die == 6:
            body += 1
            if body == 1:
                drawnSpider = replacer(3, "(", drawnSpider)
                drawnSpider = replacer(6, ")", drawnSpider )
            print(*drawnSpider, "\n")

# Printing the legs

        if (die == 3 or die == 4) and body >= 1:
            leg += 1
            if leg == 1:
                drawnSpider = replacer(7, "/", drawnSpider)
            elif leg == 2:
                drawnSpider = replacer(2, "\\", drawnSpider)
            elif leg == 3:
                drawnSpider = replacer(8, "\\", drawnSpider)
            elif leg == 4:
                drawnSpider = replacer(1, "/", drawnSpider)
            elif leg == 5:
                drawnSpider = replacer(9, "\\", drawnSpider)
            elif leg == 6:
                drawnSpider = replacer(0, "/", drawnSpider)
            print(*drawnSpider, "\n")

# Printing the Eyes

        elif die == 1 and body >= 1:
            eye += 1
            drawnSpider = replacer(4, "o", drawnSpider)
            if eye == 2:
                drawnSpider = replacer(5, "o", drawnSpider)
            print(*drawnSpider, "\n")

# Finishing the game

        if body >= 1 and leg >= 6 and eye >= 2:
            print("You made a spider, You won")
            print("Your score is: ", score)
            break
        else:
            runner = input('Do you wish to roll again? y/n: ')
    # print("\nInvalid Entry !! \nGame Over!!")

print("Welcome to the Spider Game")
print("First to complete a full Spider wins")
print("You have to get the body first with a 6")
gameRunner = input("Do you like to start the game? y/n ")
if gameRunner == 'y':
    game()
else:
    print("\nPlease enter y or n \nGame Over!!")
