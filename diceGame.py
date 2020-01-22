import random

playerPoints = []
minPlayers = 2
players = 0
maxscore = 100
amountOfDice = 2
gameRound = 0

def setPlayers():
    while True:
        players = input("How many players are playing?\n")
        if players.isdigit():
            players = int(players)
            if minPlayers <= players:
                for i in range(players):
                    playerPoints.append(0)
                return players

def diceroll(player, amountOfDice):
    throw = 0
    print("\tPlayer {0}s turn:".format(player + 1))
    for i in range(amountOfDice):
        die = random.randint(1, 6)
        print("\t\tPlayer {0} has thrown die {1} which landed on {2}".format(player + 1, i + 1, die))
        throw += die

    playerPoints[player] += throw
    print("\tPlayer {0}s score is now: {1}".format(player + 1, playerPoints[player]))
    return throw

def checkWin(maxscore):
    for player in range(players):
        if (playerPoints[player] >= maxscore):
            print("Player {0} wins!".format(player + 1))
            return True
    return False


if __name__ == "__main__":
    players = setPlayers()
    while True:
        gameRound += 1
        print("Round: {0}".format(gameRound))
        for i in range(players):
            diceroll(i, amountOfDice)
        if (checkWin(maxscore)):
            break