from random import randint

# need to show the progress of the spider through the game and add different players
def replacer(index, character, array):
    array.pop(index)
    array.insert(index, character)
    return array

def welcomeMessage():
    print("\n--------------------------------------------\n")
    print("Welcome to the Spider Game - Multi-player\n")
    print("First to complete a full Spider wins\n")
    print("You have to get the body first with a 6\n")
    print("\n--------------------------------------------\n")

def initialPrompt():
    gameRunner = input("Do you like to start the game? y/n : ")
    if gameRunner == 'y':
        playerName = input("Player Name : ")
        print("\nWelcome", playerName, '\nSo lets go\nThis is your first turn\n')
        return playerName
    else:
        print("\nPlease enter y or n \nGame Over!!")

def startGame(name):
    game(name)


def switchPlayer(player):
    if player == 1:
        return 2
    return 1


def game():
    drawnSpider = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
    drawnSpider2 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

    player = 1

    score = 0
    score2 = 0

    body = 0
    body2 = 0

    leg = 0
    leg2 = 0

    eye = 0
    eye2 = 0

    runner = 'y'
    while runner == 'y':
        print("\n###############")
        print("Player", player)
        print("###############\n")
        die = randint(1, 6)
        if player == 1:
            score += 1
        if player == 2:
            score2 += 1
        print("Turn", score)
        print("You rolled a ", die, "\n")

# Printing the body
        if die == 2 or die == 5 :
            print("Not a valid throw ", "\n")

        if die == 6 and player == 1:
            body += 1
            if body == 1:
                drawnSpider = replacer(3, "(", drawnSpider)
                drawnSpider = replacer(6, ")", drawnSpider)
            print(*drawnSpider, "\n")

        if die == 6 and player == 2:
            body2 += 1
            if body2 == 1:
                drawnSpider2 = replacer(3, "(", drawnSpider2)
                drawnSpider2 = replacer(6, ")", drawnSpider2)
            print(*drawnSpider2, "\n")


# Printing the legs

        if (die == 3 or die == 4) and body >= 1 and player == 1:
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

        if (die == 3 or die == 4) and body2 >= 1 and player == 2:
            leg2 += 1
            if leg2 == 1:
                drawnSpider2 = replacer(7, "/", drawnSpider2)
            elif leg2 == 2:
                drawnSpider2 = replacer(2, "\\", drawnSpider2)
            elif leg2 == 3:
                drawnSpider2 = replacer(8, "\\", drawnSpider2)
            elif leg2 == 4:
                drawnSpider2 = replacer(1, "/", drawnSpider2)
            elif leg2 == 5:
                drawnSpider2 = replacer(9, "\\", drawnSpider2)
            elif leg2 == 6:
                drawnSpider2 = replacer(0, "/", drawnSpider2)
            print(*drawnSpider2, "\n")
# Printing the Eyes

        elif die == 1 and body >= 1 and player == 1:
            eye += 1
            drawnSpider = replacer(4, "o", drawnSpider)
            if eye == 2:
                drawnSpider = replacer(5, "o", drawnSpider)
            print(*drawnSpider, "\n")

        elif die == 1 and body2 >= 1 and player == 2:
            eye2 += 1
            drawnSpider2 = replacer(4, "o", drawnSpider2)
            if eye2 == 2:
                drawnSpider2 = replacer(5, "o", drawnSpider2)
            print(*drawnSpider2, "\n")

# Finishing the game

        if body >= 1 and leg >= 6 and eye >= 2 and player == 1:
            print("\nCongratulations Player 1", "!!")
            print("\nYou made a spider, You won")
            print("\nYour score is: ", score)
            return score
            break
        elif body2 >= 1 and leg2 >= 6 and eye2 >= 2 and player == 2:
            print("\nCongratulations Player 2", "!!")
            print("\nYou made a spider, You won")
            print("\nYour score is: ", score2)
            return score2
            break
        else:
            runner = input('Do you wish to roll again? y/n : ')
            player = switchPlayer(player)
            if runner != 'y':
                print("\nInvalid Entry !! \nGame Over!!")

welcomeMessage()

game()
