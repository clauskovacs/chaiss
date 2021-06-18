# -*- coding: utf-8 -*-
#!/usr/bin/python3

'''
This file contains the different computer players
'''


# agent which plays a random piece each turn
class RandomAgent:
	def __init__(self):
		print('init random agent\n')

	def generate_move(self, chess_board):
		print("generating a move")

		chess_board[2, 2] = "x"

		return chess_board

