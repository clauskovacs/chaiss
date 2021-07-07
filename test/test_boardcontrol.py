# -*- coding: utf-8 -*-
#!/usr/bin/python3

import numpy as np
import unittest

from src import boardcontrol

class Unit_tests_boardcontrol(unittest.TestCase):
	"""The class containing the unit-test functions (boardcontrol).

	These include setting up the board properly as well as piece
	movement validation (including possible capturing).
	"""

	def __init__(self, *args, **kwargs):
		"""Define a pristine board state (initial set-up).

		This board state represents a board in which no piece
		has been moved at all.
		"""
		unittest.TestCase.__init__(self, *args, **kwargs)

		# (correct) initial set-up board
		self.pristine_board = np.empty([8, 8], dtype = str)

		# populate the pawns
		for i in range(0, 8):
			self.pristine_board[1, i] = 'p'
			self.pristine_board[6, i] = 'P'

		# add the rest of the board pieces
		for j in range (0, 8, 7):
			self.pristine_board[j, 0] = "r"
			self.pristine_board[j, 1] = "n"
			self.pristine_board[j, 2] = "b"
			self.pristine_board[j, 3] = "q"
			self.pristine_board[j, 4] = "k"
			self.pristine_board[j, 5] = "b"
			self.pristine_board[j, 6] = "n"
			self.pristine_board[j, 7] = "r"

		# convert the entries into upper case letters for the black pieces
		for i in range(0, 8):
			self.pristine_board[7, i - 1] = self.pristine_board[7, i - 1].upper()

	def test_boardsetup(self):
		"""Check, whether the initiated boardstate is correct.

		The initiated board state via the imported boardcontrol
		function is scrutinized for correctness.
		"""
		# intialise an unpopulated board
		chess_board = np.empty([8, 8], dtype = str)

		# reset (and populate / initiate) the board
		chess_board = boardcontrol.reset_board(chess_board)

		# assert the equality of the two boards (np.arrays)
		self.assertIsNone(
			np.testing.assert_array_equal(
				chess_board,
				self.pristine_board
			)
		)

	def test_piece_movement(self):
		"""This functions verifies the (possible) movements of pieces.

		Following functions are tested:
		o)	boardcontrol.valid_move_for_piece(). Please note that the
			ordering of the results from this function are dependent of
			its inner workings, i.e., they are not ordered in any kind!
		"""

		"""
		Define an (empty) array: represents no possible
		moves returned by the function
		boardcontrol.valid_move_for_piece().
		"""
		no_poss_moves = np.empty([0], dtype = str)

		''' check (possible) pawn movements: '''
		# create a board without any pieces on it
		chess_board = np.empty([8, 8], dtype = str)

		''' white pieces '''

		"""
		(white) pawn testing
		"""

		# populate the board
		chess_board[4, 4] = "p"	# center pawn
		chess_board[5, 5] = "R"	# enemy piece to capture
		chess_board[7, 4] = "p"	# 'edge' pawn

		# check the center pawn (at [44]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"44p",
			"white"
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				['54', '55']
			)
		)

		# check the edge pawn (at [74]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"74p",
			"white"
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				no_poss_moves
			)
		)

		# 'clear' the array
		chess_board.fill('')

		"""
		(white) rook testing
		"""

		# populate the board
		chess_board[0, 0] = "r"	# edge rook1
		chess_board[7, 7] = "r"	# edge rook2
		chess_board[3, 7] = "p"	# edge rook2
		chess_board[2, 0] = "P"	# edge rook2

		# check the center rook (at [00]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"00r",
			"white"
		)

		# define the possible moves by this rook
		valid_possible_moves = np.array(
			[
				'01', '02', '03', '04',
				'05', '06', '07', '10',
				'20'
			]
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				valid_possible_moves
			)
		)

		# check the center rook (at [77]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"77r",
			"white"
		)

		# define the possible moves by this rook
		valid_possible_moves = np.array(
			[
				'47', '57', '67', '70',
				'71', '72', '73', '74',
				'75', '76'
			]
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				valid_possible_moves
			)
		)



		''' black pieces '''

		"""
		(black) pawn testing
		"""

		# populate the board
		chess_board[4, 4] = "P"	# center pawn
		chess_board[3, 5] = "r"	# enemy piece to capture
		chess_board[0, 4] = "P"	# 'edge' pawn

		# check the center pawn (at [44]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"44P",
			"black"
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				['34', '35']
			)
		)

		# check the edge pawn (at [04]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"04P",
			"black"
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				no_poss_moves
			)
		)

		# 'clear' the array
		chess_board.fill('')



		"""
		(black) rook testing
		"""

		# populate the board
		chess_board[0, 0] = "R"	# edge rook1
		chess_board[7, 7] = "R"	# edge rook2
		chess_board[3, 7] = "P"	# edge rook2
		chess_board[2, 0] = "p"	# edge rook2

		# check the center rook (at [00]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"00R",
			"black"
		)

		# define the possible moves by this rook
		valid_possible_moves = np.array(
			[
				'01', '02', '03', '04',
				'05', '06', '07', '10',
				'20'
			]
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				valid_possible_moves
			)
		)

		# check the center rook (at [77]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"77R",
			"black"
		)

		# define the possible moves by this rook
		valid_possible_moves = np.array(
			[
				'47', '57', '67', '70',
				'71', '72', '73', '74',
				'75', '76'
			]
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				valid_possible_moves
			)
		)




if __name__ == '__main__':
	unittest.main()


