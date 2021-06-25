# -*- coding: utf-8 -*-
#!/usr/bin/python3

import numpy as np
import curses
import time

import boardcontrol
import agents

# intialise an unpopulated board
chess_board = np.empty([8, 8], dtype = str)

# reset (and populate / initiate) the board
chess_board = boardcontrol.reset_board(chess_board)

# print the current state of the board
boardcontrol.print_board(chess_board)

# initialise two computer agents
player1 = agents.RandomAgent("white")
player2 = agents.RandomAgent("black")

# generate a move for player1
#chess_board, piece_to_move, return_possible_moves = player2.generate_move(chess_board)

# print the current state of the board
#boardcontrol.print_board(chess_board, piece_to_move, return_possible_moves)


# test checking for check
king_check_test, possible_moves = player1.check_check(chess_board)
boardcontrol.add_info_msg("check whether king is in check")
boardcontrol.print_board(chess_board)

player1.game_has_ended(chess_board)
boardcontrol.print_board(chess_board)


print ('\nexiting')
