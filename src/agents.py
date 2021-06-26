# -*- coding: utf-8 -*-
#!/usr/bin/python3

"""
This file contains the different computer players
"""

import numpy as np
import random

import boardcontrol

# agent which plays a random piece each turn
class RandomAgent:
	def __init__(self, assign_player_color):
		boardcontrol.add_info_msg("initialise random agent (" + assign_player_color + ")")

		if assign_player_color != "black" and assign_player_color != "white":
			error_message = ("Error: assigned player color is neither 'black'"
				"or 'white'(assigned color: " + assign_player_color + ")"
			)
			raise ValueError(error_message)
		else:
			self.player_color = assign_player_color

	def fetch_all_pieces(self, chess_board):
		"""For a given board, this function determines all pieces (for the player).

		Used by: generate_move(). Given the player color ("black" or "white")
		this function returns an array with all positions and pieces given
		for the board state. E.g. it returns: ['00r' '01n' ... '16p' '17p']
		with each of the three characters in each array entry being the row,
		column and type of the piece, respectively.
		"""
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

	def generate_random_move(self, chess_board, piece_to_move):
		"""This function generates a random move for a piece.

		generate a (random) move for a given piece
		chess_board is the state of the board (8x8 array)
		and piece_to_move is the piece which is being
		moved, indicated by, e.g., "12p", which denotes
		a white pawn at the location 2b on the board
		"""
		print("generate random move: ", piece_to_move)

	def generate_move(self, chess_board):
		'''Generate a (valid) move for the given board state.'''
		print("generating a move")

		pieces_on_board = self.fetch_all_pieces(chess_board)

		#print(pieces_on_board, pieces_on_board.size)

		random_piece_on_board = random.randint(0,  pieces_on_board.size - 1)

		#random_piece_on_board = 1

		"""
		# change and return the board state with the taken move
		i = 3
		j = 4

		'''
		chess_board[4, 3] = "x"
		chess_board[2, 5] = "t"
		chess_board[2, 1] = "u"
		chess_board[2, 0] = "i"
		chess_board[1, 3] = "o"
		'''

		chess_board[i, j] = "k"

		pieces_on_board[random_piece_on_board] = str(i) + str(j) + chess_board[i, j]

		"""


		possible_moves = boardcontrol.valid_move_for_piece(
			chess_board,
			pieces_on_board[random_piece_on_board],
			self.player_color
		)

		print("possible moves: ", possible_moves)

		#self.generate_random_move(chess_board, pieces_on_board[random_piece_on_board])

		return chess_board, pieces_on_board[random_piece_on_board], possible_moves

	def check_check(self, chess_board):
		"""Determine, whether the (own) king is under check.
		
		All possible moves by (all) the enemy pieces are
		determined. If the king is on such a position, it
		is in check.
		"""
		# determine the position of the king which should be
		# scrutinized for check
		if self.player_color == "white":
			search_king = 'k'
		else:
			search_king = 'K'

		chess_board[1, 4] = ""
		chess_board[5, 4] = "R"
		chess_board[3, 4] = "R"
		chess_board[1, 4] = ""
		#print("Search_king:", search_king)

		# find and store the position of the king
		king_row_pos, king_col_pos = np.where(chess_board == search_king)

		# check that only one king has been found
		amount_of_kings = len(king_row_pos)
		assert  amount_of_kings == 1	\
		, 'Error: Amount of kings found (' + str(amount_of_kings) + ') is not equal to one'

		# array containing all the possible moves by all pieces on the board
		possible_moves_all_enemy_pieces = np.empty([0], dtype = str)

		"""
		go through the whole board, check each piece and collect the possible moves.
		If the player color is white, all possible moves of the _opposite color_ are
		being collected. This is used to determine whether the _own_ king is under
		check or not.
		"""
		for i in range(0, 8):
			for j in range(0, 8):
				if self.player_color == "white" and chess_board[i, j].isupper():
					# determine all possible moves by that piece
					possible_moves = boardcontrol.valid_move_for_piece(
						chess_board,
						str(i) + str(j) + str(chess_board[i, j]),
						"black"
					)

					# append possible moves to the array which are stored
					possible_moves_all_enemy_pieces = np.append(
						possible_moves_all_enemy_pieces,
						possible_moves
					)

				if self.player_color == "black" and chess_board[i, j].islower():
					# determine all possible moves by that piece
					possible_moves = boardcontrol.valid_move_for_piece(
						chess_board,
						str(i) + str(j) + str(chess_board[i, j]),
						"white"
					)

					# append possible moves to the array which are stored
					possible_moves_all_enemy_pieces = np.append(
						possible_moves_all_enemy_pieces,
						possible_moves
					)

		# remove duplicate entries in the numpy array
		possible_moves_all_enemy_pieces = np.unique(
			possible_moves_all_enemy_pieces,
			axis = 0
		)

		# determine whether the own king is on a field
		# which can be captured by an enemy piece
		search_king_pos = str(king_row_pos[0]) + str(king_col_pos[0])
		found_check_pos = np.where(
			possible_moves_all_enemy_pieces == search_king_pos
		)

		if len(found_check_pos[0]) > 0:
			king_is_in_check = True
		else:
			king_is_in_check = False

		return king_is_in_check, possible_moves_all_enemy_pieces

	def game_has_ended(self, chess_board):
		'''Determine if the game has ended (checkmate, timeout, draw).'''
		boardcontrol.add_info_msg("determine if game has ended")

		"""
		checkmate (win / lose):
			if the king of a player is threatened and it (the king)
			can't move or can't be protected (other piece is moved in between
			or the threatening piece is captured), this player loses the game.
		"""



		"""
		resignation (win / lose):
			a player offers a resignation (to end the game prematurely), e.g., when
			a check mate is immanent and can't be avoided by the player
		"""


		"""
		timeout (win / lose):
			only relevant in a timed match (a match with a certain given time limit)
		"""


		"""
		draw (tie):
			1. stalemate: 
				a player is not in check but has no other (legal) move
			2. insufficient material:
				when both players have insufficient material (amount of pieces)
				on the board.
				a) king vs. king
				b) king + minor piece (bishop or knight) vs. king
				c) lone king vs all pieces (while running out of time):
					if, e.g., white has all pieces and black only the king but
					white runs out of time this game is considered a draw. This
					is sometimes called "timeout vs. insufficient material"
				d) king + two knights vs. king
				e) king + minor piece vs. king + minor piece:
					bishop and knight are considered minor pieces
			3. 50 move-rule:
				no capture has been made or no pawn has been moved in the
				last 50 moves.
			4. repetition (threefold-repetition rule):
				if a board position arises three times in a game, either player
				can claim a draw.
			5. agreement:
				when both players decide they want a draw.
		"""


