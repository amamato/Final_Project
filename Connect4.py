#Connect 4: 2 player game where players alternate dropping red and yellow disks onto a game board.
#Game objective is to connect 4 of the same colored disks in a row, column, or on a diagonal.
#Program should display results after every round (win, lose, or continue).
import cs50
import sys

def printBoard(game):
    rows = 6
    columns = 7
    for i in range(rows):
        for j in range(columns):
            output = "|" + game[i][j]
            print(output, end="")
        print("|")
    print("---------------")


def getInput(player):
    column_selected = 0
    while True:
        if (player is 1):
            print("Drop a yellow disk at column (1-7): ", end ="")
            column_selected = cs50.get_int() - 1
            #User entry error handling
            if column_selected < 0 or column_selected > 6:
                print("Invalid entry, try again.")
            else:
                break
        else:
            print("Drop a red disk at column (1-7): ", end="")
            column_selected = cs50.get_int() - 1
            #User entry error handling
            if column_selected < 0 or column_selected > 6:
                print("Invalid entry, try again.")
            else:
                break

    print("")
    return column_selected


def findRow(game, column_selected):
    #Documentation for range is range(stop) or range(start, stop, step)
    row_selected = 0
    for row in range(0, 6):
        if game[row][column_selected] is "Y" or game[row][column_selected] is "R":
            row_selected = row - 1
            break
        row_selected = row
    return row_selected


def placeDisk(game, column_selected, row_selected, player):
    if player is 1:
        game[row_selected][column_selected] = "Y"
        player += 1
    else:
        game[row_selected][column_selected] = "R"
        player -= 1
    return player


def isBoardFull(game):
    for column in range (0, 7):
        if findRow(game, column) >= 0:
            return False
    return True


def checkWin(game):
    #Create bool variables initialized to false, one for each set of rows
    rowWin = False
    colWin = False
    LDiagWin = False
    RDiagWin = False

    #Check if four consecutive cells in a row match
    for i in range(0, 6):
        for j in range(0, 4):
            if game[i][j] == game[i][j + 1] and game[i][j] == game[i][j + 2] and game[i][j] == game[i][j + 3] and game[i][j] != " ":
                rowWin = True
                break

    #Check if four columns in the same row match
    for i in range (0, 3):
        for j in range (0, 7):
            if game[i][j] == game[i + 1][j] and game[i][j] == game[i + 2][j] and game[i][j] == game[i + 3][j] and game[i][j] != " ":
                colWin = True
                break

    #Check if four diagonals match (top left to btm right)
    for i in range (0, 3):
        for j in range (0, 4):
            if game[i][j] == game[i + 1][j + 1] and game[i][j] == game[i + 2][j + 2] and game[i][j] == game[i + 3][j + 3] and game[i][j] != " ":
                LDiagWin = True
                break

    #Check if diagonals in other direction match (top right to btm left)
        for i in range (0, 3):
            for j in range (3, 7):
                if game[i][j] == game[i + 1][j - 1] and game[i][j] == game[i + 2][j - 2] and game[i][j] == game[i + 3][j - 3] and game[i][j] != " ":
                    RDiagWin = True
                    break

    #If any of the checks returned True, return that a winner was found
    if rowWin is True or colWin is True or LDiagWin is True or RDiagWin is True:
        return True
    else:
        return False


def printFinalResult(player, winner):
    #Determines if winner was found or if the game is a tie. If someone won, whoever's turn it is, the opposite player wins!
    if winner is True:
        if player is 1:
            print("The red player wins!")
        else:
            print("The yellow player wins!")
    else:
        print("It's a tie game!")


def main():
    #Create Connect 4 game board (should be 6 rows x 7 columns)
    game = [[" "]*7 for _ in range(6)]
    #Initialize key variables to start game
    winner = False
    isFull = False

    #Print game board to user and start with player 1
    printBoard(game)
    player = 1
    while winner == False and isFull == False:
        column_selected = getInput(player)
        row_selected = findRow(game, column_selected)
        if row_selected >= 0:
            player = placeDisk(game, column_selected, row_selected, player)
            printBoard(game)
            isFull = isBoardFull(game)
            winner = checkWin(game)
        else:
            isFull = isBoardFull(game)
            if isFull is False:
                #User error handling
                print("That column is already full, please try another")
                print("")

    printFinalResult(player, winner)


if __name__ == "__main__":
    main()