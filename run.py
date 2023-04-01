"""
Import random to generate random integers in game
"""
from random import randint

# Game Legend
# ▢ - blank space
# ⨀ - missed shot
# ⊗ - hit ship

HIDDEN_BOARD = [["▢"] * 8 for x in range(8)]
GUESS_BOARD = [["▢"] * 8 for x in range(8)]
letters_to_numbers = {
    "A": 0,1
    yyyy
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


print_board(GUESS_BOARD)
print_board(HIDDEN_BOARD)


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
    row = input("\nEnter ship row 1-8: ")
    while row not in "12345678":
        print("\nPlease enter a valid row")
        row = input("\nEnter ship row 1-8: \n")
    column = input("\nEnter ship column A-H: ").upper()
    while column not in "ABCDEFGH":
        print("\nPlease enter a valid column")
        column = input("\nEnter ship column A-H: ").upper()
    return (int(row) - 1, letters_to_numbers[column])


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
    print("⛴  WELCOME TO BATTLESHIPS ⛴\n")
    print("YOU HAVE 25 GUESSES TO SINK 5 BATTLESHIPS\n")
    print("Game Legend:")
    print("▢ - blank space")
    print("⨀ - missed shot")
    print("♨ - hit ship\n")
    print_board(GUESS_BOARD)
    (row, column) = fire_shot()
    if GUESS_BOARD[row][column] == "⨀ ":
        print("\nYou've already guessed that \n")
    elif HIDDEN_BOARD[row][column] == "♨":
        print("\nGREAT SHOT! you sunk a battleship \n")
        GUESS_BOARD[row][column] = "♨"
        turns -= 1
    else:
        print("\nAh unlucky, you missed! \n")
        GUESS_BOARD[row][column] = "⨀"
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print("\n CONGRATULATIONS! You've sunk all 5 battleships! \n")
        break
    print("You have " + str(turns) + " turns remaining \n")
    if turns == 0:
        print("\n GAME OVER! you have 0 turns remaining \n")
        break
