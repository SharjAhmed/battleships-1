from random import randint

board = []

for x in range(0, 8):
    board.append(["▢"]*8)


def print_board(board):
    '''
    Create board to see where user can guess where to hit
    '''
    print('    A   B   C   D   E   F   G   H')
    print('  --------------------------------')
    row_number = 1
    for row in board:
        print('%d | %s | ' % (row_number, ' | '.join(row)))
        row_number += 1

print_board(board)