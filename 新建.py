from random import random


def choose_who_go_first():
    if random.randint(0,1) == 0:
        return "player"
    else:
        return "computer"


def get_player_move(board):
    move = input("Where do you want to move?")
    while move not in ["1","2","3","4","5","6","7","8","9"] and not is_empty:
        print("Please enter your move(1~9).")
        move = input("Where do you want to move?")
    return move

def move(board, position, letter):
    board[position] = letter


def is_win(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter)or
            (board[4] == letter and board[5] == letter and board[6] == letter)or
            (board[7] == letter and board[8] == letter and board[9] == letter)or
            (board[1] == letter and board[4] == letter and board[7] == letter)or
            (board[2] == letter and board[5] == letter and board[8] == letter)or
            (board[3] == letter and board[6] == letter and board[9] == letter)or
            (board[7] == letter and board[5] == letter and board[3] == letter)or
            (board[1] == letter and board[5] == letter and board[9] == letter))


