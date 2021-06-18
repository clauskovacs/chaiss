# -*- coding: utf-8 -*-
#!/usr/bin/python3

import numpy

import boardcontrol
import agents

testboard = boardcontrol.ChessBoard()

print("\n")



# intialise an unpopulated board
chess_board = numpy.empty([8, 8], dtype = str)

# reset (and populate / initiate) the board
chess_board = testboard.reset_board(chess_board)

# print the current state of the board
testboard.print_board(chess_board)

print("\n")

# initialise two computer agents
player1 = agents.RandomAgent()
player2 = agents.RandomAgent()

# generate a move for player1
chess_board = player1.generate_move(chess_board)

# print the current state of the board
testboard.print_board(chess_board)


print ('\nexiting')
