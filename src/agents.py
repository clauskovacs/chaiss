# -*- coding: utf-8 -*-
#!/usr/bin/python3

'''
This file contains the different computer players
'''

import numpy as np
import random

import boardcontrol

# agent which plays a random piece each turn
class RandomAgent:
	def __init__(self, assign_player_color):
		print('init random agent\n')

		self.player_color = assign_player_color	# "black" or "white"

	#########################################################################
	# used by: generate_move(). Given the player color ("black" or "white")	#
	# this function returns an array with all positions and pieces given	#
	# for the board state. E.g. it returns: ['00r' '01n' ... '16p' '17p']	#
	# with each of the three entries in the array being the row, column and	#
	# identification of the pieces, respectively.
	#########################################################################
	def fetch_all_pieces(self, chess_board):
		pieces_on_board = np.empty([0], dtype = str)

		for row in range(0, 8):
			for col in range(0, 8):
				# player = white -> select lower case entries in the array
				if chess_board[row, col].islower() and self.player_color == "white":
					found_piece = str(row) + str(col) + chess_board[row, col]
					pieces_on_board = np.append(pieces_on_board, found_piece)
				# player = black -> select upper case entries in the array
				if chess_board[row, col].isupper() and self.player_color == "black":
					found_piece = str(row) + str(col) + chess_board[row, col]
					pieces_on_board = np.append(pieces_on_board, found_piece)

		return pieces_on_board

	#####################################################
	# generate a (random) move for a given piece		#
	# chess_board is the state of the board (8x8 array)	#
	# and piece_to_move is the piece which is being		#
	# moved, indicated by, e.g., "12p", which denotes	#
	# a white pawn at the location 2b on the board		#
	#####################################################
	def generate_random_move(self, chess_board, piece_to_move):
		print("generate random move: ", piece_to_move)

	#####################################################
	# generate a (valid) move for the given board state	#
	#####################################################
	def generate_move(self, chess_board):
		print("generating a move")

		pieces_on_board = self.fetch_all_pieces(chess_board)

		#print(pieces_on_board, pieces_on_board.size)

		random_piece_on_board = random.randint(0,  pieces_on_board.size)
		random_piece_on_board = 1

		# change and return the board state with the taken move
		i = 3
		j = 3

		'''
		chess_board[4, 3] = "x"
		chess_board[2, 5] = "t"
		chess_board[2, 1] = "u"
		chess_board[2, 0] = "i"
		chess_board[1, 3] = "o"
		'''

		chess_board[i, j] = "b"
		pieces_on_board[random_piece_on_board] = str(i) + str(j) + chess_board[i, j]


		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			pieces_on_board[random_piece_on_board],
			self.player_color
		)

		print("possible moves: ", possible_moves)

		#self.generate_random_move(chess_board, pieces_on_board[random_piece_on_board])

		return chess_board, pieces_on_board[random_piece_on_board], possible_moves

