import random
import os
import time

# Initialize game boards
GAME_BOARD = [[" " for _ in range(7)] for _ in range(7)]
VISIBLE_BOARD = [[" " for _ in range(7)] for _ in range(7)]

# Mapping letters to numbers for easier indexing
LETTERS_TO_NUMBERS = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}

# Define the number of ships of each size
ships_amount = {1: 3, 2: 2}

def is_already_shot(coord):
    # Check if the coordinate has already been shot
    x = int(coord[1]) - 1
    y = LETTERS_TO_NUMBERS[coord[0]]

    if VISIBLE_BOARD[x][y] == "m" or VISIBLE_BOARD[x][y] == "X":
        return True
    else:
        return False

def display_interface(board):
    # Display the game interface
    print("   A B C D E F G")
    print("  --------------")

    for i in range(len(board)):
        row = ""
        for j in range(len(board[i])):
            row = row + board[i][j] + " "

        print(f"{i + 1}| {row}")

def make_hit(coord):
    # Update the visible board based on the hit
    x = int(coord[1]) - 1
    y = LETTERS_TO_NUMBERS[coord[0]]
    if GAME_BOARD[x][y] == "O":
        VISIBLE_BOARD[x][y] = "X"
    else:
        VISIBLE_BOARD[x][y] = "m"

def generate_single_ship():
    # Generate a single ship on the game board
    x = random.randint(0, 6)
    y = random.randint(0, 6)

    if got_interruption(x, y):
        generate_single_ship()
    else:
        GAME_BOARD[x][y] = "O"

def got_interruption(x, y):
    # Check if there is an interruption for ship placement
    interrupted = False

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y:
                if ship_exists(i, j):
                    interrupted = True
                else:
                    continue
            elif 0 <= i <= 6 and 0 <= j <= 6:
                if ship_exists(i, j):
                    interrupted = True

    return interrupted

def ship_exists(x_cord, y_cord):
    # Check if a ship exists at the given coordinates
    if GAME_BOARD[x_cord][y_cord] == "O":
        return True
    else:
        return False

def generate_big_ship(length):
    # Generate a bigger ship on the game board
    x_cord = random.randint(0, 6)
    y_cord = random.randint(0, 6)
    directions = []
    created_big_ship = True

    if not got_interruption(x_cord, y_cord):
        if x_cord + length <= 6:
            directions.append("down")
        if y_cord + length <= 6:
            directions.append("right")
        if x_cord - length >= -1:
            directions.append("up")
        if y_cord - length >= -1:
            directions.append("left")
    else:
        return False

    choice = random.choice(directions)

    if choice == "left":
        count = y_cord + 1
        for i in range(length):
            GAME_BOARD[x_cord][count - 1] = "O"
            count -= 1
    elif choice == "right":
        count = y_cord - 1
        for i in range(length):
            GAME_BOARD[x_cord][count + 1] = "O"
            count += 1
    elif choice == "up":
        count = x_cord + 1
        for i in range(length):
            GAME_BOARD[count - 1][y_cord] = "O"
            count -= 1
    elif choice == "down":
        count = x_cord - 1
        for i in range(length):
            GAME_BOARD[count + 1][y_cord] = "O"
            count += 1

    return created_big_ship

# Place ships on the game board
for elem in ships_amount.items():
    c = 0
    while c != elem[0]:
        if generate_big_ship(elem[1]):
            c += 1

# Place single ships on the game board
for _ in range(4):
    generate_single_ship()

# Game loop
while True:
    print("Missed shots are marked as 'm'.\nHitting shots are marked as 'X'.")
    display_interface(board=VISIBLE_BOARD)
    hit_coordinate = input("Enter a coordinate in 'letter/digit' form: ")
    
    if not is_already_shot(hit_coordinate):
        make_hit(hit_coordinate)
    else:
        os.system("cls")
        print("You've already shot in this point!")
        time.sleep(2.0)
       
    os.system("cls")
