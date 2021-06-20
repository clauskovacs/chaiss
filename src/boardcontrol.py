# -*- coding: utf-8 -*-
#!/usr/bin/python3

'''
This file contains all the logic setting up and managing the board.
'''

import numpy as np

# dict for the pieces (abbreviated as they are stored in the board state)
chess_pieces = {
	"K" : "king",
	"Q" : "queen",
	"R" : "rook",
	"B" : "bishop",
	"N" : "knight",
	"P" : "pawn"
}

# inverse the dict containing the pieces
chess_pieces_inverse = {v: k for k, v in chess_pieces.items()}

#########################################################
# reset a board to its initial starting configuration	#
# small letters = white pieces							#
# capital letters = black pieces						#
#########################################################
def reset_board(reset_board):
	print("resetting board")

	# pawns
	for i in range(0, 8):
		reset_board[1, i] = chess_pieces_inverse["pawn"].lower()
		reset_board[6, i] = chess_pieces_inverse["pawn"]

	# rest of the pieces
	for i in range(0, 8, 7):
		reset_board[i, 0] = chess_pieces_inverse["rook"]
		reset_board[i, 1] = chess_pieces_inverse["knight"]
		reset_board[i, 2] = chess_pieces_inverse["bishop"]
		reset_board[i, 3] = chess_pieces_inverse["queen"]
		reset_board[i, 4] = chess_pieces_inverse["king"]
		reset_board[i, 5] = chess_pieces_inverse["bishop"]
		reset_board[i, 6] = chess_pieces_inverse["knight"]
		reset_board[i, 7] = chess_pieces_inverse["rook"]

	# convert the entries into lower case letters for the white pieces
	for i in range(0, 8):
		reset_board[0, i-1] = reset_board[0, i-1].lower()

	return reset_board

#########################################
# print a board state (to the console)	#
#########################################
def print_board(print_board):
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
			fetch_piece = " " if print_board[7-row, col] == "" else print_board[7-row, col]
			print(fetch_piece, " | ", end = "", sep = "")
		print("", eval_row)
		print("     ---------------------------------")

	# print footer
	print(header_string)

def add_to_poss_moves(possible_moves, piece_row_pos, piece_col_pos):
	possible_moves = np.append(
		possible_moves, str(piece_row_pos) + str(piece_col_pos)
		)
	return possible_moves

#################################################################
# determine the valid moves for a given piece and board state	#
#################################################################
def valid_move_for_piece(chess_board, piece_position):
	# TODO: add en passant and promotion for pawns
	print("DET VALID MOVE: ", piece_position)

	# unpack the state of the piece which is should be moved
	piece_row_pos = int(piece_position[0])
	piece_col_pos = int(piece_position[1])
	piece_id = piece_position[2]

	# check, whether the given piece position matches the one in the board
	assert  piece_id == chess_board[piece_row_pos, piece_col_pos]	\
	, 'Error: mismatching information of pieces in valid_move_for_piece()'

	# return array with all possible moves by that piece
	possible_moves = np.empty([0], dtype = str)

	# white pawn
	if piece_id == chess_pieces_inverse["pawn"].lower():
		# unmoved (white) pawn: check for a two-move
		if piece_row_pos == 1 and chess_board[piece_row_pos+1, piece_col_pos] == "":
			if (
				chess_board[piece_row_pos+2, piece_col_pos].isupper()
				or chess_board[piece_row_pos+2, piece_col_pos] == ""
				):
				possible_moves = add_to_poss_moves(
					possible_moves,
					piece_row_pos+2,
					piece_col_pos
				)

		# check for all other moves (advance one directly or capture
		# to the adjacent diagonals in direction of advancing)
		if piece_row_pos < 7:	# pawn has not reached the end of the board
			if chess_board[piece_row_pos+1, piece_col_pos] == "":	# empty tile in front
				possible_moves = add_to_poss_moves(
					possible_moves,
					piece_row_pos+1,
					piece_col_pos
				)
			# check the diagonals (in front)
			if piece_col_pos-1 > -1:	# diagonal 'up, left' is not out of bounds
				if chess_board[piece_row_pos+1, piece_col_pos-1].isupper():
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos+1,
						piece_col_pos-1
					)
			if (piece_col_pos+1 < 7):	# diagonal 'up, right' is not out of bounds
				if chess_board[piece_row_pos+1, piece_col_pos+1].isupper():
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos+1,
						piece_col_pos+1
					)

	# black pawn
	if piece_id == chess_pieces_inverse["pawn"]:
		# unmoved (white) pawn: check for a two-move
		if piece_row_pos == 6 and chess_board[piece_row_pos-1, piece_col_pos] == "":
			if (
				chess_board[piece_row_pos-2, piece_col_pos].isupper()
				or chess_board[piece_row_pos-2, piece_col_pos] == ""
				):
				possible_moves = add_to_poss_moves(
					possible_moves,
					piece_row_pos-2,
					piece_col_pos
				)

		# check for all other moves (advance one directly or capture
		# to the adjacent diagonals in direction of advancing)
		if piece_row_pos > 0:	# pawn has not reached the end of the board
			if chess_board[piece_row_pos-1, piece_col_pos] == "":	# empty tile in front
				possible_moves = add_to_poss_moves(
					possible_moves,
					piece_row_pos-1,
					piece_col_pos
				)
			# check the diagonals (in front)
			if piece_col_pos-1 > -1:	# diagonal 'up, left' is not out of bounds
				if chess_board[piece_row_pos-1, piece_col_pos-1].islower():
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos-1,
						piece_col_pos-1
					)
			if (piece_col_pos+1 < 8):	# diagonal 'up, right' is not out of bounds
				if chess_board[piece_row_pos-1, piece_col_pos+1].islower():
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos-1,
						piece_col_pos+1
					)

	# rook
	# TODO: make this routine (for the rook) more efficiently -> benchmark this (timewise)!
	if piece_id.lower() == chess_pieces_inverse["rook"].lower():


		# obstacle_* == True -> piece in direction detected
		obstacle_north = False
		obstacle_south = False
		obstacle_east = False
		obstacle_west = False

		# search seven in each direction. If a piece is detected in any of
		# the four cardinal direction, the obstacle_* variable is set True
		# and any further search in that direction is not continued.
		for i in range(7):
			# check all four cardinal directions
			#
			# 'north'
			if piece_row_pos+i+1 < 8 and obstacle_north == False:
				if chess_board[piece_row_pos+i+1, piece_col_pos] == "":
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos+i+1,
						piece_col_pos
					)
				else:
					obstacle_north = True
			#
			# 'south'
			if piece_row_pos-i-1 > -1 and obstacle_south == False:
				if chess_board[piece_row_pos-i-1, piece_col_pos] == "":
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos-i-1,
						piece_col_pos
					)
				else:
					obstacle_south = True
			#
			# 'east'
			if piece_col_pos+i+1 < 8 and obstacle_east == False:
				if chess_board[piece_row_pos, piece_col_pos+i+1] == "":
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos,
						piece_col_pos+i+1
					)
				else:
					obstacle_east = True
			#
			# 'west'
			if piece_col_pos-i-1 > -1 and obstacle_west == False:
				if chess_board[piece_row_pos, piece_col_pos-i-1] == "":
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos,
						piece_col_pos-i-1
					)
				else:
					obstacle_west = True

	return possible_moves


