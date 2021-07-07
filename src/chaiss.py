# -*- coding: utf-8 -*-
#!/usr/bin/python3

import curses
import numpy as np
import multiprocessing
import os
from queue import Queue
import sys
import threading
import time

import agents
import boardcontrol
import windowhandler
import stdoutwrapper

if __name__ == '__main__':
	# std console wrapper (put text to the console after the curses terminal is closed)
	mystdout = stdoutwrapper.StdOutWrapper()
	sys.stdout = mystdout
	sys.stderr = mystdout
	mystdout.write("write\nsome\ndummy\ntext for testing")	# add some dummy tet for testing

	########################################
	# control logic (keyboard, and screen) #
	########################################

	# reduce the time it takes to close the curses terminal when the
	# ESC key has been pressed (to 10 milliseconds)
	os.environ.setdefault('ESCDELAY', '10')

	# set the curses screen identifier
	screen = curses.initscr()

	box1 = curses.newwin(20, 20, 5, 5)
	box1.box()    

	screen.refresh()
	box1.refresh()

	# define a queue object (with infinite size) to
	# exchange information between the thread(s)
	q = Queue(maxsize = 0)

	window = windowhandler.WindowHandler(screen)

	"""
	window.print_message("Number of CPU cores: "
		+ str(multiprocessing.cpu_count()) + "\n", 1
	)
	"""

	# define the thread which manages drawing on the screen
	# and keyboard inputs by the user
	window_print_thread = threading.Thread(
		target = window.main_window_loop,
		args = (q,)
	)
	window_print_thread.daemon = True
	window_print_thread.start()

	######################
	# game logic/control #
	######################

	# intialise an unpopulated board
	chess_board = np.empty([8, 8], dtype = str)

	# reset (and populate / initiate) the board
	chess_board = boardcontrol.reset_board(chess_board)

	## print the current state of the board
	#boardcontrol.print_board(chess_board)

	## initialise two computer agents
	player1 = agents.RandomAgent("white")
	player2 = agents.RandomAgent("black")

	## generate a move for player1
	chess_board, piece_to_move, return_possible_moves = player2.generate_move(chess_board)

	## print the current state of the board
	##boardcontrol.print_board(chess_board, piece_to_move, return_possible_moves)

	# the 'game logic loop' which manages agents, player interactions, etc.
	while window_print_thread.is_alive():
		#window.change_queue(q)	# put (add) an element to the queue

		# print the current state of the board
		boardcontrol.print_board(chess_board, window, piece_to_move, return_possible_moves)

		window.print_message("  " + str(q.qsize()))

		time.sleep(0.1)

	# delete the object to be able to write to the terminal
	del window

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

	# print the logged text into the standard console after the curses
	# window is closed.
	sys.stdout = sys.__stdout__
	sys.stderr = sys.__stderr__
	sys.stdout.write(mystdout.get_text(0, 5))

	# empty all queues
	q.queue.clear()
