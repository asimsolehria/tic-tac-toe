board = [" - "] * 9
player = " "
symbol = ' '
player1 = input("Enter Player 1 name : ")
while player1 == '':
    print("Player name can't be Empty! ")
    player1 = input("Enter Player 1 name : ")

player2 = input("Enter Player 2 name : ")
while player2 == '':
    print("Player name can't be Empty! ")
    player2 = input("Enter Player 2 name : ")

winner = " "
Tie = 0


def drawBoard():
    print(board[6], "|", board[7], "|", board[8])
    print(board[3], "|", board[4], "|", board[5])
    print(board[0], "|", board[1], "|", board[2])


def toss():
    global player
    global symbol
    player = player2
    symbol = 'X'
    print("It is ", player, " 's turn \n")


def play_game():
    toss()

    drawBoard()
    for i in range(9):
        if winner == "X":
            print(player1, " won the game!")
        elif winner == 'O':
            print(player2, " won the game!")

            break
        player = player2
        markSymbol()
        checkWin()
        checkTie()
        if winner == ' ' and Tie == 0:
            handlePlayer()


def markSymbol():
    global board
    position = int(input("Chose your Position from 1-9 "))

    while position < 1 or position > 9:
        print("\n Invalid Input")
        position = int(input("Chose your Position from 1-9 "))

    position = position - 1

    while board[position] != " - ":

        print("\n Invalid Position, Chose another position")
        position = int(input("Chose your Position from 1-9 "))
        while position < 0 or position > 9:
            print("\n Invalid Input")
            position = int(input("Chose your Position from 1-9 "))
        position = position - 1
    else:
        board[position] = symbol
    drawBoard()


def checkWin():
    global winner
    # ROWS
    if board[0] == board[1] == board[2] != ' - ':
        winner = board[0]
    if board[3] == board[4] == board[5] != ' - ':
        winner = board[3]
    if board[6] == board[7] == board[8] != ' - ':
        winner = board[6]

    # COLUMNS
    if board[0] == board[3] == board[6] != ' - ':
        winner = board[0]
    if board[1] == board[4] == board[7] != ' - ':
        winner = board[1]
    if board[2] == board[5] == board[8] != ' - ':
        winner = board[2]

    # DIAGONAL
    if board[0] == board[4] == board[8] != ' - ':
        winner = board[0]
    if board[2] == board[4] == board[6] != ' - ':
        winner = board[2]


def handlePlayer():
    global player
    global symbol
    if player == player1 and symbol == 'O':
        player = player2
        symbol = 'X'

    elif player == player2 and symbol == "X":
        player = player1
        symbol = "O"
    print("It is ", player, "'s turn")


def checkTie():
    global Tie
    if " - " not in board and winner == ' ':
        print("Game ended Tie :( ")
        Tie = 1


play_game()
