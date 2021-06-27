# -*- coding: utf-8 -*-
#!/usr/bin/python3

"""
courtesy of:
https://stackoverflow.com/questions/14010073/print-to-standard-console-in-curses
"""

class StdOutWrapper:
	"""Wrapper for text to be written to the 'std console' after, e.g., curses is closed.
	
	Add text using write() into the buffer and retrive it using get_text().
	"""
	text = ""

	def write(self, txt):
		'''Add text to the logfile (variable text).'''
		self.text += txt
		self.text = '\n'.join(self.text.split('\n')[-30:])

	def get_text(self, beg, end):
		"""Retrieve the text added to the wrapper.

		The variables beg and end define the amount of lines which
		will be printed to the console.
		"""
		return '\n'.join(self.text.split('\n')[beg:end])+'\n'
