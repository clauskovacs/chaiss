# -*- coding: utf-8 -*-
#!/usr/bin/python3

import numpy as np
import curses
import os


class WindowHandler:
	def __init__(self, stdscr):
		# reduce the time it takes to close the window then the ESC key
		# has been pressed (to 25 milliseconds)
		os.environ.setdefault('ESCDELAY', '25')

		self.scr = stdscr

		## enable arrow keys (up, down, left, right)
		self.scr.keypad(1)

		## fetch the current (terminal) window size
		self.wnd_height, self.wnd_width = self.scr.getmaxyx()

		## enable non-blocking mode, i.e., getch() does not halt
		## the process until a key is pressed
		self.scr.nodelay(True)

		# do not print pressed keys to the screen
		#curses.noecho()

		#curses.use_default_colors()

	#def __del__(self):
		#curses.endwin()

	def main_loop(self):
		while 1:
			c = self.scr.getch()

			if c == curses.KEY_ENTER or c == 10 or c == 13:
				self.scr.addstr("\nENTER\n")

			if c == curses.KEY_LEFT:
				self.scr.addstr("LEFT")

			if c == curses.KEY_RIGHT:
				self.scr.addstr("RIGHT")

			if c == curses.KEY_UP:
				self.scr.addstr("UP")

			if c == curses.KEY_DOWN:
				self.scr.addstr("DOWN")

			x, y = self.scr.getyx()
			#self.scr.addstr("KUH\n" + str(x) + " / " + str(y) + " | ")

			self.scr.addstr("M")

			if x > self.wnd_height - 3:
				self.scr.erase()

			#if c == ord('q'):
				#pass

			if c == 27:
				#scr.addstr("DOWN")
				break

			# user resizes the window manually
			if c == curses.KEY_RESIZE:

				self.scr.erase()	# clear the window

				# retrieve the width and height of the resized window
				wnd_height, wnd_width = self.scr.getmaxyx()

				self.scr.addstr("SIZE (w: " + str(wnd_width) + " / h: " + str(wnd_height) + ")")
