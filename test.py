import random

player_letter = ""
computer_letter = ""


def print_welcome_msg():
    print("Welcome to Tic Tac Toe!")
    print("This is the first game that made by Peler and Jessie!")
    print("ENJOY!")


def get_player_letter():
    global player_letter
    global computer_letter
    letter = input("Do you want to use X or O? ").upper()
    while not (letter == "X" or letter == "O"):
        print("please enter X or O")
        letter = input("Do you want to use X or O? ").upper()
    if letter == "X":
        player_letter = "X"
        computer_letter = "O"
    else:
        player_letter = "O"
        computer_letter = "X"


def print_board(board):
    print(f" {board[7]} | {board[8]} | {board[9]}")
    print("-----------")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print("-----------")
    print(f" {board[1]} | {board[2]} | {board[3]}")


def choose_who_go_first():
    """
    the function will decide whether to player go first or computer go first
    :return: True if player go first, False if computer go first
    """
    return random.choice([True, False])

#
def get_player_move(board):
    """
    get player move
    :return: the index of the position which player wants to move
    """
    move = input("What's your next move? ")
    while move not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] and (not is_empty(board, int(move))):
        print("please enter a valid move")
        move = input("What's your next move? ")
    return int(move)


def make_move(board, position, letter):
    board[position] = letter


def is_empty(board, position):
    return board[position] == " "


def is_win(board, letter):

    return (board[7] == board[8] == board[9] == letter) or (board[4] == board[5] == board[6] == letter) or (
            board[1] == board[2] == board[3] == letter) or (board[7] == board[4] == board[1] == letter) or (
            board[9] == board[6] == board[3] == letter) or (board[8] == board[5] == board[2] == letter) or (
            board[7] == board[5] == board[3] == letter) or (board[9] == board[5] == board[1] == letter)


def get_board_copy(board):
    return board[:]


def get_computer_move(board):
    for i in range(1, 10):
        if is_empty(board, i):
            copy_board = get_board_copy(board)
            make_move(copy_board, i, computer_letter)
            if is_win(copy_board, computer_letter):
                return i

    for i in range(1, 10):
        if is_empty(board, i):
            copy_board = get_board_copy(board)
            make_move(copy_board, i, player_letter)
            if is_win(copy_board, player_letter):
                return i

    if is_empty(board, 5):
        return 5

    empty_list = []
    for i in [2, 4, 6, 8]:
        if is_empty(board, i):
            empty_list.append(i)
    if empty_list:
        print(empty_list)
        return random.choice(empty_list)

    empty_list = []
    for i in [1, 3, 7, 9]:
        if is_empty(board, i):
            empty_list.append(i)
    if empty_list:
        return random.choice(empty_list)


def is_game_board_full(board):
    for i in range(1, 10):
        if board[i] == " ":
            return False
    return True


def is_game_over():
    if is_win(board, player_letter):
        print("you win!")
        return True
    elif is_win(board, computer_letter):
        print("you lost!")
        return True
    elif is_game_board_full(board):
        print("the game board is full!")
        return True
    return False


if __name__ == '__main__':
    board = [' '] * 10

    print_welcome_msg()
    get_player_letter()
    is_player_turn = choose_who_go_first()
    while True:
        if is_player_turn:
            print("Player's turn")
            print_board(board)
            move = get_player_move(board)
            make_move(board, move, player_letter)
            if is_game_over():
                break
            is_player_turn = False
        else:
            move = get_computer_move(board)
            if move:
                make_move(board, move, computer_letter)
            print_board(board)
            if is_game_over():
                break
            is_player_turn = True
