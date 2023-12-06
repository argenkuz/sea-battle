import random
import os
import time

GAME_BOARD = [[" ", " ", " ", " ", " ", " ", " "] for x in range(7)]
VISIBLE_BOARD = [[" ", " ", " ", " ", " ", " ", " "] for x in range(7)]
LETTERS_TO_NUMBERS = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}

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
