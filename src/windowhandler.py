# -*- coding: utf-8 -*-
#!/usr/bin/python3

import curses
import numpy as np
import time
from queue import Queue

class WindowHandler:
	def __init__(self, screen):
		# set the curses screen identifier
		self.scr = screen

		# enable arrow keys (up, down, left, right)
		self.scr.keypad(1)

		## fetch the current (terminal) window size
		self.wnd_height, self.wnd_width = self.scr.getmaxyx()

		# enable non-blocking mode, i.e., getch() does not halt
		# the process until a key is pressed
		self.scr.nodelay(True)

		# print the pressed buttons to the screen or not
		print_to_screen = True
		if print_to_screen == True:
			curses.echo()
		else:
			curses.noecho()

		"""
		initiate colors in curses and define color pairs
		"""
		curses.start_color()

		# arguments: (color_id, font_color, background_color)
		curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
		curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

	def __del__(self):
		curses.endwin()

	def clear_screen(self):
		self.scr.erase()

	def print_message(self, message_to_print, color_pair = 0):
		"""Print a message on the screen using curses.

		This function takes the message to pring as well as
		a color in the argument. The default (hardwired) color
		coding is marked by zero (0), which is white text color
		on black background.
		"""
		self.scr.addstr(message_to_print, curses.color_pair(color_pair))

		# get the current cursor position
		x, y = self.scr.getyx()

		if x > self.wnd_height - 2:
			self.clear_screen()

	def change_queue(self, q):
		q.put("X  ")

	def main_window_loop(self, q):
		"""Contains the loop which handles drawing and keyboard interactions.

		This functions runs in an own thread and handles user inputs as well
		as output into the terminal. Pressing of keys (arrow keys, ESC, etc.)
		are handled. The logic runs separately, independently from this loop
		and transfer of information between them (these two) is realised using
		Queue objects.
		"""
		while 1:
			#start_time = time.process_time()

			c = self.scr.getch()	# detect (get) key press

			if c == curses.KEY_ENTER or c == 10 or c == 13:
				self.scr.addstr("ENTER\n")

			if c == curses.KEY_LEFT:
				self.scr.addstr("LEFT")

			if c == curses.KEY_RIGHT:
				self.scr.addstr("RIGHT")

			if c == curses.KEY_UP:
				self.scr.addstr("UP")

			if c == curses.KEY_DOWN:
				self.scr.addstr("DOWN")

			# get the current cursor position
			x, y = self.scr.getyx()

			# end of the screen (height) reached -> clear the screen
			if x > self.wnd_height - 2:
				self.scr.erase()

			if c == 27:	# ESC key
				break

			"""
			if q.empty() == False:	# queue is _not_ empty
				fetch = q.get()		# remove an item from the queue
				self.scr.addstr(str(fetch))
			"""

			# user resizes the window manually
			if c == curses.KEY_RESIZE:
				self.scr.erase()	# clear the window

				# retrieve the width and height of the resized window
				self.wnd_height, self.wnd_width = self.scr.getmaxyx()

				self.scr.addstr("SIZE (w: "
					+ str(self.wnd_width)
					+ " / h: " + str(self.wnd_height)
					+ ")"
				)

			"""
			# write the time it took the program to execute to the screen
			self.scr.addstr(str(
				time.process_time()
				- start_time)
				+ "\n"
			)
			"""
