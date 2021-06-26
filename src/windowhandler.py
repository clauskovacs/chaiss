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

		## enable non-blocking mode, i.e., getch() does not halt
		## the process until a key is pressed
		self.scr.nodelay(True)

		# print the pressed buttons to the screen or not
		print_to_screen = True
		if print_to_screen == True:
			curses.echo()
		else:
			curses.noecho()

		#curses.use_default_colors()

	def __del__(self):
		curses.endwin()

	def print_msg_to_screen(self, message_to_print):
		self.scr.addstr(message_to_print)

	def change_queue(self, q):
		q.put("1")

	def main_loop(self, q):
		while 1:
			c = self.scr.getch()

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

			# read the cursor position
			x, y = self.scr.getyx()

			# end of the screen (height) reached -> clear the screen
			if x > self.wnd_height - 2:
				self.scr.erase()

			#if c == ord('q'):
				#pass

			if c == 27:
				#scr.addstr("DOWN")
				break

			if q.empty() == False:	# queue is _not_ empty
				fetch = q.get()		# remove an item from the queue
				self.scr.addstr(str(fetch))

			#self.scr.addstr(str(q.qsize()) + " <-> " + str(q.empty()))
			self.scr.addstr("A")
			time.sleep(0.1)

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

			self.scr.refresh()

		return False
