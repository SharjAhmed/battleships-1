from random import randint

board = []

for x in range(0, 5):
    board.append(["o"]*5)


def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)
