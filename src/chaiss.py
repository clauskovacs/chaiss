# -*- coding: utf-8 -*-
#!/usr/bin/python3

import numpy as np

import boardcontrol
import agents

print("\n")

# intialise an unpopulated board
chess_board = np.empty([8, 8], dtype = str)

# reset (and populate / initiate) the board
chess_board = boardcontrol.reset_board(chess_board)

# print the current state of the board
boardcontrol.print_board(chess_board)

print("\n")

# initialise two computer agents
player1 = agents.RandomAgent("white")
player2 = agents.RandomAgent("black")

# generate a move for player1
chess_board = player1.generate_move(chess_board)

# print the current state of the board
boardcontrol.print_board(chess_board)

print ('\nexiting')
