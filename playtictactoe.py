# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 20:46:04 2025

@author: akash123
"""

print("Welcome to Tic Tac Toe!\nPlayer 1: X\nPlayer 2: O")
state = "Current Board:\n 1 | 2 | 3\n---+---+---\n 4 | X | 6\n---+---+---\n 7 | 8 | 9"
print(state)
a = input("Player 2, enter your move (1-9):")
state = state.replace(a, "O")
print(state)