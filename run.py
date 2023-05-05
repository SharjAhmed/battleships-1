"""
Import random to generate random integers in game
"""
from random import randint


HIDDEN_BOARD = [["▢"] * 8 for x in range(8)]
GUESS_BOARD = [["▢"] * 8 for x in range(8)]
letters_to_numbers = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
}

board = []


def print_board(board):
    """
    Create board for player to guess where to hit
    """
    print("    A   B   C   D   E   F   G   H")
    row_number = 1
    for row in board:
        print("%d | %s | " % (row_number, " | ".join(row)))
        row_number += 1


print("\n⛴  WELCOME TO BATTLESHIPS ⛴\n")
print("YOU HAVE 25 GUESSES TO SINK 5 BATTLESHIPS\n")
print("Game Legend:")
print("▢ - blank space")
print("⊗ - missed shot")
print("♨ - hit ship\n")
print_board(board)


def create_ships(board):
    """
    Place ships randomly
    """
    for ship in range(5):
        (ship_row, ship_column) = (randint(0, 7), randint(0, 7))
        while board[ship_row][ship_column] == "♨":
            (ship_row, ship_column) = (randint(0, 7), randint(0, 7))
        board[ship_row][ship_column] = "♨"


def fire_shot():
    """
    Asking player what row and column to fire their shot
    """

    row = input("\nEnter ship row 1-8: ").upper()
    while len(row) == 0:
        row = input("\nEnter ship row 1-8: ").upper()
    while row not in "12345678":
        print('Please select a valid row 1 to 8')
        row = input("Ship Row: ").upper()

    column = input("\nEnter ship column A-H: ").upper()
    while len(column) == 0:
        column = input("\nEnter ship column A-H: ").upper()
    while column not in "ABCDEFGH":
        print('Please select a valid column A to H')
        column = input("\nEnter ship column A-H: ").upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hit_ships(board):
    """
    Count every time the player hits a ship
    Game is over when all 5 ships are hit
    """
    count = 0
    for row in board:
        for column in row:
            if column == "♨":
                count += 1
    return count


create_ships(HIDDEN_BOARD)
turns = 25
while turns > 0:
    print_board(GUESS_BOARD)
    (row, column) = fire_shot()
    if GUESS_BOARD[row][column] == "⊗":
        print("\n------------------------------------------------")
        print("You've already guessed that! Please guess again")
        print("------------------------------------------------\n")
    elif HIDDEN_BOARD[row][column] == "♨":
        print("\n---------------------------------------")
        print("GREAT SHOT! you sunk a battleship!")
        print("---------------------------------------\n")
        GUESS_BOARD[row][column] = "♨"
        turns -= 1
    else:
        print("\n------------------------")
        print("Ah unlucky, you missed!")
        print("------------------------\n")
        GUESS_BOARD[row][column] = "⊗"
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print("\n------------------------------------------------------")
        print("\n CONGRATULATIONS! You've sunk all 5 battleships! \n")
        print("------------------------------------------------------\n")
        break
    print("You have " + str(turns) + " turns remaining \n")
    if turns == 0:
        print("\n--------------------------------------------")
        print("\n GAME OVER! you have 0 turns remaining \n")
        print("--------------------------------------------\n")
        break
