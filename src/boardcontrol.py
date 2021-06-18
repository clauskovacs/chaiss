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

		# place the pieces at the board
		self.reset_board()

	# reset a board to its initial starting configuration
	def reset_board(self):
		print("resetting board", self.chess_pieces["K"])

		# white pieces (small letters)
		for i in range(0, 8):
			self.board[1, i] = "p"


	# print a board state (cout it to the console)
	def print_board(self):
		print("print board state")

		#print(self.board)

		# create header
		header_string = "    |"
		for col in range(0, 8):
			header_string += str(col) + " |"
		print(header_string)
		print("    -------------------------")

		for row in range(0, 8):
			print(row, ": |", end = "")
			for col in range(0, 8):
				print(row, "", col, "|", end = "", sep = "")
			print(": ", row)

		print("    -------------------------")
		print(header_string)
