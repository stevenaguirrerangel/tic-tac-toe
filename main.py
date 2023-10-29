import random

BOARD = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]
board_start = ["1", "2", "3",
               "4", "5", "6",
               "7", "8", "9"]
CURRENT_PLAYER = "X"
WINNER = None
GAME_RUNNING = True
num_of_players = int(input("Type the number of players (1 or 2): "))


# printing the game board
def print_board(board):
    print(f" {board[0]}  |  {board[1]}  |  {board[2]}")
    print("---------------")
    print(f" {board[3]}  |  {board[4]}  |  {board[5]}")
    print("---------------")
    print(f" {board[6]}  |  {board[7]}  |  {board[8]}")


# take player input
def player_input(board):
    choice = input("Enter a number 1-9: ")
    choice_num = int(choice)
    if 1 <= choice_num <= 9 and board[choice_num - 1] == choice:
        board[choice_num - 1] = CURRENT_PLAYER
    else:
        print("This spot is already in play")


# check for win or tie
def check_horizontal(board):
    global WINNER
    if board[0] == board[1] == board[2]:
        WINNER = board[0]
        return True
    elif board[3] == board[4] == board[5]:
        WINNER = board[3]
        return True
    elif board[6] == board[7] == board[8]:
        WINNER = board[6]
        return True


def check_vertical(board):
    global WINNER
    if board[0] == board[3] == board[6]:
        WINNER = board[0]
        return True
    elif board[1] == board[4] == board[7]:
        WINNER = board[1]
        return True
    elif board[2] == board[5] == board[8]:
        WINNER = board[2]
        return True


def check_diagonal(board):
    global WINNER
    if board[0] == board[4] == board[8]:
        WINNER = board[0]
        return True
    elif board[6] == board[4] == board[2]:
        WINNER = board[2]
        return True


def check_tie(board):
    global GAME_RUNNING
    no_tie = any((True for x in board_start if x in board))
    if no_tie:
        pass
    else:
        print_board(board)
        print("It is a tie!")
        GAME_RUNNING = False


# check for the win or tie again
def check_win(board):
    global GAME_RUNNING
    if check_diagonal(board) or check_horizontal(board) or check_vertical(board):
        print_board(BOARD)
        GAME_RUNNING = False
        print(f"The winner is {WINNER}")


# switch the player
def player_switch():
    global CURRENT_PLAYER
    if CURRENT_PLAYER == "X":
        CURRENT_PLAYER = "O"
    else:
        CURRENT_PLAYER = "X"


def computer(board):
    while CURRENT_PLAYER == "O":
        position = random.randint(0, 8)
        if board[position] != "X":
            board[position] = "O"
            player_switch()


while GAME_RUNNING:
    if num_of_players == 1:
        print_board(BOARD)
        player_input(BOARD)
        check_win(BOARD)
        check_tie(BOARD)
        player_switch()
    if num_of_players == 2:
        print_board(BOARD)
        player_input(BOARD)
        check_win(BOARD)
        check_tie(BOARD)
        player_switch()
        computer(BOARD)
        check_win(BOARD)
        check_tie(BOARD)
    if num_of_players <= 0 or num_of_players > 2:
        print("Only inputs allowed are '1' or '2'")
        num_of_players = int(input("Type the number of players (1 or 2): "))


