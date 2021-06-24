# -*- coding: utf-8 -*-
#!/usr/bin/python3

'''
This file contains all the logic setting up and managing the board.
'''

import numpy as np

#install colorama using 'sudo python3 -m pip install colorama'
from colorama import Fore, Style, init
init()

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
		reset_board[0, i - 1] = reset_board[0, i - 1].lower()

	return reset_board

#########################################
# print a board state (to the console)	#
#########################################
def print_board(print_board, highlight_piece_to_move = '', highlight_fields = ''):
	print("print board state (small letters = white)")
	#print("hightlight fields: ", highlight_fields)

	# print header
	header_entries = ["a", "b", "c", "d", "e", "f", "g", "h"]
	header_string = "   ".join(header_entries)
	header_string = "       " + header_string
	print(header_string)
	print("     ---------------------------------")

	# print middle part
	for row in range(0, 8):
		eval_row = 8 - row
		print(" ", eval_row, " | ", end = "")
		for col in range(0, 8):
			# hightlight possible moves with that piece (given by 'highlight_piece_to_move')
			search_str_arr = str(7 - row) + str(col)
			if search_str_arr in highlight_fields:
				# no enemy piece on the field to move (-> mark this field with '+')
				if print_board[7 - row, col] == "":
					fetch_piece = Fore.RED + "+" + Style.RESET_ALL
				# enemy piece on field -> colorise it red
				else:
					fetch_piece = Fore.RED + print_board[7 - row, col] + Style.RESET_ALL

				print(fetch_piece + " | ", end = "", sep = "")
			else:
				# highlight piece which is about to move blue
				if highlight_piece_to_move[:-1] == search_str_arr:
					fetch_piece = Fore.BLUE + print_board[7 - row, col] + Style.RESET_ALL
				# default coloring
				else:
					fetch_piece = " " if print_board[7 - row, col] == "" else print_board[7 - row, col]

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
def valid_move_for_piece(chess_board, piece_position, player_color):
	# TODO: add en passant and promotion for pawns
	print("DETERMINE VALID MOVE: ", piece_position)

	# unpack the state of the piece which is should be moved
	piece_row_pos = int(piece_position[0])
	piece_col_pos = int(piece_position[1])
	piece_id = piece_position[2]

	assert ((player_color == 'black' and piece_id.isupper())
		or (player_color == 'white' and piece_id.islower())
	), print('Error: piece to move and player color do not match')

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
				chess_board[piece_row_pos + 2, piece_col_pos].isupper()
				or chess_board[piece_row_pos + 2, piece_col_pos] == ""
				):
				possible_moves = add_to_poss_moves(
					possible_moves,
					piece_row_pos + 2,
					piece_col_pos
				)

		# check for all other moves (advance one directly or capture
		# to the adjacent diagonals in direction of advancing)
		if piece_row_pos < 7:	# pawn has not reached the end of the board
			if chess_board[piece_row_pos + 1, piece_col_pos] == "":	# empty tile in front
				possible_moves = add_to_poss_moves(
					possible_moves,
					piece_row_pos + 1,
					piece_col_pos
				)
			# check the diagonals (in front)
			if piece_col_pos - 1 > -1:	# diagonal 'up, left' is not out of bounds
				if chess_board[piece_row_pos + 1, piece_col_pos - 1].isupper():
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos + 1,
						piece_col_pos - 1
					)
			if (piece_col_pos + 1 < 7):	# diagonal 'up, right' is not out of bounds
				if chess_board[piece_row_pos+1, piece_col_pos + 1].isupper():
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos + 1,
						piece_col_pos + 1
					)

	# black pawn
	if piece_id == chess_pieces_inverse["pawn"]:
		# unmoved (white) pawn: check for a two-move
		if piece_row_pos == 6 and chess_board[piece_row_pos - 1, piece_col_pos] == "":
			if (
				chess_board[piece_row_pos - 2, piece_col_pos].isupper()
				or chess_board[piece_row_pos - 2, piece_col_pos] == ""
				):
				possible_moves = add_to_poss_moves(
					possible_moves,
					piece_row_pos - 2,
					piece_col_pos
				)

		# check for all other moves (advance one directly or capture
		# to the adjacent diagonals in direction of advancing)
		if piece_row_pos > 0:	# pawn has not reached the end of the board
			if chess_board[piece_row_pos-1, piece_col_pos] == "":	# empty tile in front
				possible_moves = add_to_poss_moves(
					possible_moves,
					piece_row_pos - 1,
					piece_col_pos
				)
			# check the diagonals (in front)
			if piece_col_pos - 1 > -1:	# diagonal 'up, left' is not out of bounds
				if chess_board[piece_row_pos - 1, piece_col_pos - 1].islower():
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos - 1,
						piece_col_pos - 1
					)
			if (piece_col_pos + 1 < 8):	# diagonal 'up, right' is not out of bounds
				if chess_board[piece_row_pos - 1, piece_col_pos + 1].islower():
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos - 1,
						piece_col_pos + 1
					)

	# knight
	if piece_id.lower() == chess_pieces_inverse["knight"].lower():
		# numpy array containing the eight possible moves of that knight
		possible_moves_knight = np.zeros(shape = (8, 2), dtype = int)

		# generate an array containing the eight possible moves with the
		# knight from it's starting position
		index = 0
		for i in range(-2, 4, 4):
			for j in range(-1, 2, 2):
				possible_moves_knight[index] = (piece_row_pos + i, piece_col_pos + j)
				index += 1
				possible_moves_knight[index] = (piece_row_pos + j, piece_col_pos + i)
				index += 1

		# go through each position. If it is inside the board and not occupied
		# by an own piece, push this position to the array 'possible_moves'
		for i in range(8):
			check_position_row = possible_moves_knight[i][0]
			check_position_col = possible_moves_knight[i][1]

			if (check_position_row > -1
				and check_position_row < 8
				and check_position_col > -1
				and check_position_col < 8
				):
				# empty target tile
				if chess_board[check_position_row, check_position_col] == "":
					possible_moves = add_to_poss_moves(
						possible_moves,
						check_position_row,
						check_position_col
					)
				# player is white, target piece is black
				elif (piece_id.islower()
				and chess_board[check_position_row, check_position_col].isupper()
				):
					possible_moves = add_to_poss_moves(
						possible_moves,
						check_position_row,
						check_position_col
					)
				# player is black, target piece is white
				elif (piece_id.isupper()
				and chess_board[check_position_row, check_position_col].islower()
				):
					possible_moves = add_to_poss_moves(
						possible_moves,
						check_position_row,
						check_position_col
					)

	# rook or queen (queen = rook + bishop)
	if (piece_id.lower() == chess_pieces_inverse["rook"].lower()
		or piece_id.lower() == chess_pieces_inverse["queen"].lower()
	):
		# obstacle_* == True -> piece in direction detected
		obstacle_north = False
		obstacle_south = False
		obstacle_east = False
		obstacle_west = False

		# search seven in each direction. If a piece is detected in any of
		# the four cardinal directions, the obstacle_* variable is set True
		# and any further search in that direction is not continued. Until
		# then (empty positions) are added to the array of possible moves.
		for i in range(7):
			# check all four cardinal directions
			#
			# 'north'
			if piece_row_pos + i + 1 < 8 and obstacle_north == False:
				# save the content of the field scrutinised into a variable for brevity
				piece_to_check_north = chess_board[piece_row_pos + i + 1, piece_col_pos]
				#
				if piece_to_check_north == "":
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos + i + 1,
						piece_col_pos
					)
				else:
					obstacle_north = True	# don't search any further in this direction
					# add the last piece detected if it can be captured
					if ((piece_to_check_north.isupper() and player_color == "white")
						or (piece_to_check_north.islower() and player_color == "black")
					):
						possible_moves = add_to_poss_moves(
							possible_moves,
							piece_row_pos + i + 1,
							piece_col_pos
						)
			#
			# 'south'
			if piece_row_pos - i - 1 > -1 and obstacle_south == False:
				# save the content of the field scrutinised into a variable for brevity
				piece_to_check_south = chess_board[piece_row_pos - i - 1, piece_col_pos]
				#
				if piece_to_check_south == "":
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos - i - 1,
						piece_col_pos
					)
				else:
					obstacle_south = True	# don't search any further in this direction
					# add the last piece detected if it can be captured
					if ((piece_to_check_south.isupper() and player_color == "white")
						or (piece_to_check_south.islower() and player_color == "black")
					):
						possible_moves = add_to_poss_moves(
							possible_moves,
							piece_row_pos - i - 1,
							piece_col_pos
						)
			#
			# 'east'
			if piece_col_pos + i + 1 < 8 and obstacle_east == False:
				# save the content of the field scrutinised into a variable for brevity
				piece_to_check_east = chess_board[piece_row_pos, piece_col_pos + i + 1]
				#
				if piece_to_check_east == "":
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos,
						piece_col_pos + i + 1
					)
				else:
					obstacle_east = True
					# add the last piece detected if it can be captured
					if ((piece_to_check_east.isupper() and player_color == "white")
						or (piece_to_check_east.islower() and player_color == "black")
					):
						possible_moves = add_to_poss_moves(
							possible_moves,
							piece_row_pos,
							piece_col_pos + i + 1
						)
			#
			# 'west'
			if piece_col_pos - i - 1 > -1 and obstacle_west == False:
				# save the content of the field scrutinised into a variable for brevity
				piece_to_check_west = chess_board[piece_row_pos, piece_col_pos - i - 1]
				#
				if piece_to_check_west == "":
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos,
						piece_col_pos - i - 1
					)
				else:
					obstacle_west = True
					# add the last piece detected if it can be captured
					if ((piece_to_check_west.isupper() and player_color == "white")
						or (piece_to_check_west.islower() and player_color == "black")
					):
						possible_moves = add_to_poss_moves(
							possible_moves,
							piece_row_pos,
							piece_col_pos - i - 1
						)

	# bishop or queen
	if (piece_id.lower() == chess_pieces_inverse["bishop"].lower()
		or piece_id.lower() == chess_pieces_inverse["queen"].lower()
	):
		# obstacle_* == True -> piece in direction detected
		obstacle_NE = False	# northeast
		obstacle_SE = False	# southeast
		obstacle_SW = False # southwest
		obstacle_NW = False # northwest

		# search seven in each direction. If a piece is detected in any of
		# the four directions (NE, SE, SW, NW), the obstacle_* variable is
		# set True and any further search in that direction is not continued.
		# Until then (empty positions) are added to the array of possible moves.
		for i in range(7):
			# check all four directions (NE, SE, SW, NW)
			#
			# 'northeast'
			if (piece_row_pos + i + 1 < 8
				and piece_col_pos + i + 1 < 8
				and obstacle_NE == False
			):
				# save the content of the field scrutinised into a variable for brevity
				piece_to_check_north = chess_board[
					piece_row_pos + i + 1,
					piece_col_pos + i + 1
				]
				#
				if piece_to_check_north == "":
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos + i + 1,
						piece_col_pos + i + 1
					)
				else:
					obstacle_NE = True	# don't search any further in this direction
					# add the last piece detected if it can be captured
					if ((piece_to_check_north.isupper() and player_color == "white")
						or (piece_to_check_north.islower() and player_color == "black")
					):
						possible_moves = add_to_poss_moves(
							possible_moves,
							piece_row_pos + i + 1,
							piece_col_pos + i + 1
						)
			#
			# 'southeast'
			if (piece_row_pos - i - 1 > -1
				and piece_col_pos + i + 1 < 8
				and obstacle_SE == False
			):
				# save the content of the field scrutinised into a variable for brevity
				piece_to_check_north = chess_board[
					piece_row_pos - i - 1,
					piece_col_pos + i + 1
				]
				#
				if piece_to_check_north == "":
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos - i - 1,
						piece_col_pos + i + 1
					)
				else:
					obstacle_SE = True	# don't search any further in this direction
					# add the last piece detected if it can be captured
					if ((piece_to_check_north.isupper() and player_color == "white")
						or (piece_to_check_north.islower() and player_color == "black")
					):
						possible_moves = add_to_poss_moves(
							possible_moves,
							piece_row_pos - i - 1,
							piece_col_pos + i + 1
						)
			#
			# 'southwest'
			if (piece_row_pos - i - 1 > -1
				and piece_col_pos - i - 1 > -1
				and obstacle_SW == False
			):
				# save the content of the field scrutinised into a variable for brevity
				piece_to_check_north = chess_board[
					piece_row_pos - i - 1,
					piece_col_pos - i - 1
				]
				#
				if piece_to_check_north == "":
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos - i - 1,
						piece_col_pos - i - 1
					)
				else:
					obstacle_SW = True	# don't search any further in this direction
					# add the last piece detected if it can be captured
					if ((piece_to_check_north.isupper() and player_color == "white")
						or (piece_to_check_north.islower() and player_color == "black")
					):
						possible_moves = add_to_poss_moves(
							possible_moves,
							piece_row_pos - i - 1,
							piece_col_pos - i - 1
						)
			#
			# 'northwest'
			if (piece_row_pos + i + 1 < 8
				and piece_col_pos - i - 1 > -1
				and obstacle_NW == False
			):
				# save the content of the field scrutinised into a variable for brevity
				piece_to_check_north = chess_board[
					piece_row_pos + i + 1,
					piece_col_pos - i - 1
				]
				#
				if piece_to_check_north == "":
					possible_moves = add_to_poss_moves(
						possible_moves,
						piece_row_pos + i + 1,
						piece_col_pos - i - 1
					)
				else:
					obstacle_NW = True	# don't search any further in this direction
					# add the last piece detected if it can be captured
					if ((piece_to_check_north.isupper() and player_color == "white")
						or (piece_to_check_north.islower() and player_color == "black")
					):
						possible_moves = add_to_poss_moves(
							possible_moves,
							piece_row_pos + i + 1,
							piece_col_pos - i - 1
						)

	# king
	if piece_id.lower() == chess_pieces_inverse["king"].lower():
		# iterate over the eight next neighbours
		for i in [-1, 0, 1]:
			for j in [-1, 0, 1]:
				"""
				only add the position, if the target is in the boundary
				of the board and it is not the piece which is going to
				be moved itself
				"""
				if (
					(j != 0 or i != 0)
					and
					(
						0 <= piece_row_pos + i < 8
						and 0 <= piece_col_pos + j < 8
					)
				):
					# what is on the board at the position we check at the moment?
					move_to_check = chess_board[piece_row_pos + i, piece_col_pos + j]

					# enemy piece on this position or it is empty
					# (add this position to the list of possible moves)
					if ((piece_id.isupper() == move_to_check.islower())
						or move_to_check == ""
					):
						possible_moves = add_to_poss_moves(
							possible_moves,
							piece_row_pos + i,
							piece_col_pos + j
						)

	return possible_moves

