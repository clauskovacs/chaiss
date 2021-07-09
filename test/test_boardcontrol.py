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

		# check the pawn (at [44]):
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

		# check the pawn (at [74]):
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

		# 'clear' the board
		chess_board.fill('')

		"""
		(white) rook testing
		"""

		# populate the board
		chess_board[0, 0] = "r"	# edge rook1
		chess_board[7, 7] = "r"	# edge rook2
		chess_board[3, 7] = "p"	# edge rook2
		chess_board[2, 0] = "P"	# edge rook2

		# check the rook (at [00]):
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

		# check the rook (at [77]):
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

		# 'clear' the board
		chess_board.fill('')


		"""
		(white) knight testing
		"""

		# populate the board
		chess_board[0, 0] = "n"
		chess_board[7, 7] = "n"
		chess_board[2, 1] = "n"
		chess_board[1, 2] = "R"
		chess_board[5, 6] = "R"

		# check the knight (at [00]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"00n",
			"white"
		)

		# define the possible moves by this knight
		valid_possible_moves = np.array(
			[
				'12'
			]
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				valid_possible_moves
			)
		)

		# check the knight (at [77]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"77n",
			"white"
		)

		# define the possible moves by this knight
		valid_possible_moves = np.array(
			[
				'56', '65'
			]
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				valid_possible_moves
			)
		)

		# 'clear' the board
		chess_board.fill('')


		"""
		(white) bishop testing
		"""

		# populate the board
		chess_board[4, 4] = "b"
		chess_board[0, 0] = "k"
		chess_board[2, 6] = "R"

		# check the bishop (at [44]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"44b",
			"white"
		)

		# define the possible moves by this bishop
		valid_possible_moves = np.array(
			[
				'11', '22', '26', '33',
				'35', '53', '55', '62',
				'66', '71', '77'
			]
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				valid_possible_moves
			)
		)

		# 'clear' the board
		chess_board.fill('')


		"""
		(white) queen testing
		"""

		# populate the board
		chess_board[4, 4] = "q"
		chess_board[0, 0] = "R"
		chess_board[7, 7] = "p"

		# check the queen (at [44]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"44q",
			"white"
		)

		# define the possible moves by this queen
		valid_possible_moves = np.array(
			[
				'00', '04', '11', '14',
				'17', '22', '24', '26',
				'33', '34', '35', '40',
				'41', '42', '43', '45',
				'46', '47', '53', '54',
				'55', '62', '64', '66',
				'71', '74'
			]
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				valid_possible_moves
			)
		)

		# 'clear' the board
		chess_board.fill('')


		"""
		(white) king testing
		"""

		# populate the board
		chess_board[4, 4] = "k"
		chess_board[3, 3] = "P"
		chess_board[5, 5] = "r"


		# check the king (at [44]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"44k",
			"white"
		)

		# define the possible moves by this queen
		valid_possible_moves = np.array(
			[
				'33', '34', '35', '43',
				'45', '53', '54'
			]
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				valid_possible_moves
			)
		)

		# change the board state
		chess_board[7, 7] = "k"
		chess_board[6, 6] = "q"
		chess_board[6, 7] = "P"


		# check the king (at [77]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"77k",
			"white"
		)

		# define the possible moves by this queen
		valid_possible_moves = np.array(
			[
				'67', '76'
			]
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				valid_possible_moves
			)
		)

		# 'clear' the board
		chess_board.fill('')




		''' black pieces '''

		"""
		(black) pawn testing
		"""

		# populate the board
		chess_board[4, 4] = "P"	# center pawn
		chess_board[3, 5] = "r"	# enemy piece to capture
		chess_board[0, 4] = "P"	# 'edge' pawn

		# check the pawn (at [44]):
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

		# check the pawn (at [04]):
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

		# 'clear' the board
		chess_board.fill('')



		"""
		(black) rook testing
		"""

		# populate the board
		chess_board[0, 0] = "R"	# edge rook1
		chess_board[7, 7] = "R"	# edge rook2
		chess_board[3, 7] = "P"	# edge rook2
		chess_board[2, 0] = "p"	# edge rook2

		# check the rook (at [00]):
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

		# check the rook (at [77]):
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


		"""
		(black) knight testing
		"""

		# populate the board
		chess_board[0, 0] = "N"
		chess_board[7, 7] = "N"
		chess_board[2, 1] = "N"
		chess_board[1, 2] = "r"
		chess_board[5, 6] = "r"

		# check the knight (at [00]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"00N",
			"black"
		)

		# define the possible moves by this knight
		valid_possible_moves = np.array(
			[
				'12'
			]
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				valid_possible_moves
			)
		)

		# check the knight (at [00]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"77N",
			"black"
		)

		# define the possible moves by this knight
		valid_possible_moves = np.array(
			[
				'56', '65'
			]
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				valid_possible_moves
			)
		)

		# 'clear' the board
		chess_board.fill('')


		"""
		(black) bishop testing
		"""

		# populate the board
		chess_board[4, 4] = "B"
		chess_board[0, 0] = "K"
		chess_board[2, 6] = "r"

		# check the bishop (at [44]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"44B",
			"black"
		)

		# define the possible moves by this bishop
		valid_possible_moves = np.array(
			[
				'11', '22', '26', '33',
				'35', '53', '55', '62',
				'66', '71', '77'
			]
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				valid_possible_moves
			)
		)

		# 'clear' the board
		chess_board.fill('')


		"""
		(black) queen testing
		"""

		# populate the board
		chess_board[4, 4] = "Q"
		chess_board[0, 0] = "r"
		chess_board[7, 7] = "P"

		# check the queen (at [44]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"44Q",
			"black"
		)

		# define the possible moves by this queen
		valid_possible_moves = np.array(
			[
				'00', '04', '11', '14',
				'17', '22', '24', '26',
				'33', '34', '35', '40',
				'41', '42', '43', '45',
				'46', '47', '53', '54',
				'55', '62', '64', '66',
				'71', '74'
			]
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				valid_possible_moves
			)
		)

		# 'clear' the board
		chess_board.fill('')


		"""
		(black) king testing
		"""

		# populate the board
		chess_board[4, 4] = "K"
		chess_board[3, 3] = "p"
		chess_board[5, 5] = "R"


		# check the king (at [44]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"44K",
			"black"
		)

		# define the possible moves by this queen
		valid_possible_moves = np.array(
			[
				'33', '34', '35', '43',
				'45', '53', '54'
			]
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				valid_possible_moves
			)
		)

		# change the board state
		chess_board[7, 7] = "K"
		chess_board[6, 6] = "Q"
		chess_board[6, 7] = "p"


		# check the king (at [77]):
		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			"77K",
			"black"
		)

		# define the possible moves by this queen
		valid_possible_moves = np.array(
			[
				'67', '76'
			]
		)

		# assert the possible moves
		self.assertIsNone(
			np.testing.assert_array_equal(
				possible_moves,
				valid_possible_moves
			)
		)

		# 'clear' the board
		chess_board.fill('')



if __name__ == '__main__':
	unittest.main()
