# -*- coding: utf-8 -*-
#!/usr/bin/python3

import unittest

class Unit_test_class(unittest.TestCase):

	def test_func1(self):
		self.assertEqual(1, 1)

if __name__ == '__main__':
	unittest.main()


