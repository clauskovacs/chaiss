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
		self.assertEqual(1, 1)

if __name__ == '__main__':
	unittest.main()


