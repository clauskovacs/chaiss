# -*- coding: utf-8 -*-
#!/usr/bin/python3

'''
This file contains all the logic setting up and managing the board.
'''

import numpy

class ChessBoard:
	def __init__(self):
		print ('init board obj\n')

		# dict for the pieces (abbreviated as they are stored in the board state)
		self.chess_pieces = {
			"K" : "king",
			"Q" : "queen",
			"R" : "rook",
			"B" : "bishop",
			"N" : "knight",
			"P" : "pawn"
		}

		# intialise an unpopulated board
		self.board = numpy.empty([8, 8], dtype = str)

		# place the pieces at the board (in the starting configuration)
		self.reset_board()

	#########################################################
	# reset a board to its initial starting configuration	#
	# small letters = white pieces							#
	# capital letters = black pieces						#
	#########################################################
	def reset_board(self):
		print("resetting board")

		# pawns
		for i in range(0, 8):
			self.board[1, i] = "p"
			self.board[6, i] = "P"

		# inverse the dict containing the pieces
		inverse_chess_pieces = {v: k for k, v in self.chess_pieces.items()}

		# rest of the pieces
		for i in range(0, 8, 7):
			self.board[i, 0] = inverse_chess_pieces["rook"]
			self.board[i, 1] = inverse_chess_pieces["knight"]
			self.board[i, 2] = inverse_chess_pieces["bishop"]
			self.board[i, 3] = inverse_chess_pieces["queen"]
			self.board[i, 4] = inverse_chess_pieces["king"]
			self.board[i, 5] = inverse_chess_pieces["bishop"]
			self.board[i, 6] = inverse_chess_pieces["knight"]
			self.board[i, 7] = inverse_chess_pieces["rook"]

		# convert the entries into lower case letters for the white pieces
		for i in range(0, 8):
			self.board[0, i-1] = self.board[0, i-1].lower()

	# print a board state (to the console)
	def print_board(self):
		print("print board state (small letters = white)")

		# print header
		header_entries = ["a", "b", "c", "d", "e", "f", "g", "h"]
		header_string = "   ".join(header_entries)
		header_string = "       " + header_string
		print(header_string)
		print("     ---------------------------------")

		# print middle part
		for row in range(0, 8):
			eval_row = 8-row
			print(" ", eval_row, " | ", end = "")
			for col in range(0, 8):
				fetch_piece = " " if self.board[7-row, col] == "" else self.board[7-row, col]
				print(fetch_piece, " | ", end = "", sep = "")
			print(" ", eval_row)
			print("     ---------------------------------")

		# print footer
		print(header_string)
