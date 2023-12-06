import random
import os
import time

GAME_BOARD = [[" ", " ", " ", " ", " ", " ", " "] for x in range(7)]
VISIBLE_BOARD = [[" ", " ", " ", " ", " ", " ", " "] for x in range(7)]
LETTERS_TO_NUMBERS = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}

ships_amount = {1: 3, 2: 2}
