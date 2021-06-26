# -*- coding: utf-8 -*-
#!/usr/bin/python3

import curses
import numpy as np
import multiprocessing
import os
from queue import Queue
import threading
import time


import agents
import boardcontrol
import windowhandler as wndhandler



if __name__ == '__main__':
	
	# reduce the time it takes to close the window then the ESC key
	# has been pressed (to 10 milliseconds)
	os.environ.setdefault('ESCDELAY', '10')

	# set the curses screen identifier
	screen = curses.initscr()

	# define a queue object to transfer information to the thread
	q = Queue(maxsize = 0)

	test = wndhandler.WindowHandler(screen)

	test.print_msg_to_screen("Number of CPU cores: "
		+ str(multiprocessing.cpu_count()) + "\n"
	)
	
	window_print_thread = threading.Thread(target = test.main_loop, args = (q,))
	window_print_thread.daemon = True
	window_print_thread.start()


	while window_print_thread.is_alive():
	#while True:
		#q.put("1")
		test.change_queue(q)
		time.sleep(0.5)

	curses.endwin()




	"""
	# intialise an unpopulated board
	chess_board = np.empty([8, 8], dtype = str)

	# reset (and populate / initiate) the board
	chess_board = boardcontrol.reset_board(chess_board)

	# print the current state of the board
	boardcontrol.print_board(chess_board)

	# initialise two computer agents
	player1 = agents.RandomAgent("white")
	player2 = agents.RandomAgent("black")

	# generate a move for player1
	#chess_board, piece_to_move, return_possible_moves = player2.generate_move(chess_board)

	# print the current state of the board
	#boardcontrol.print_board(chess_board, piece_to_move, return_possible_moves)

	# test checking for check
	king_check_test, possible_moves = player1.check_check(chess_board)
	boardcontrol.add_info_msg("check whether king is in check")
	boardcontrol.print_board(chess_board)

	player1.game_has_ended(chess_board)
	boardcontrol.print_board(chess_board)
	"""
