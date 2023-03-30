"""
Import random to generate random integers in game
"""
from random import randint

# Game Legend
# ▢ - blank space
# ⨀ - missed shot
# ⊗ - hit ship

HIDDEN_BOARD = [['▢'] * 8 for x in range(8)]
GUESS_BOARD = [['▢'] * 8 for x in range(8)]
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
}

board = []

def print_board(board):
    '''
    Create board for player to guess where to hit
    '''
    print('    A   B   C   D   E   F   G   H')
    row_number = 1
    for row in board:
        print('%d | %s | ' % (row_number, ' | '.join(row)))
        row_number += 1


def create_ships(board):
    '''
    Random hidden ships for user to find
    '''
    for ship in range(5):
        (ship_row, ship_column) = (randint(0, 7), randint(0, 7))
        while board[ship_row][ship_column] == 'X':
            (ship_row, ship_column) = (randint(0, 7), randint(0, 7))
        board[ship_row][ship_column] = 'X'


def get_ship_loction():
    '''
    Ask user what row and column they want to choose to find the ship
    '''
    row = input('Enter ship row 1-8: ')
    while row not in '12345678':
        print('Please enter a valid row')
        row = input('Enter ship row 1-8: \n')
    column = input('Enter ship column A-H: ').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column')
        column = input('Enter ship column A-H: ').upper()
    return (int(row) - 1, letters_to_numbers[column])


def count_hit_ships(board):
    '''
    Count every time the user hits a ship.
    When you hit all 5 the game is over.
    '''
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


create_ships(HIDDEN_BOARD)
turns = 10
while turns > 0:
    print('WELCOME TO BATTLESHIPS')
    print("ATTEMPT TO SINK MY SHIP WITHIN 5 GUESSES")
    print_board(GUESS_BOARD)
    (row, column) = get_ship_loction()
    if GUESS_BOARD[row][column] == '0':
        print('\n You already guessed that \n')
    elif HIDDEN_BOARD[row][column] == 'X':
        print('\n DIRECT HIT! you sunk a battleship \n')
        GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print('\n Sorry, YOU MISSED! \n')
        GUESS_BOARD[row][column] = '0'
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print('\n CONGRATULATIONS! YOU HAVE SUNK ALL THE BATTLESHIPS! \n')
        break
    print('You have ' + str(turns) + ' turns remaining \n')
    if turns == 0:
        print('\n GAME OVER! you have 0 turns left remaining \n')
        break