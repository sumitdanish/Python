

__author__ = 'SU915198'


import sys
import random
import os


class MyFib:

	def fib(self, f_data):

		if f_data == 0 or f_data == 1:
			return 1;
		return self.fib(f_data-1)+self.fib(f_data-2)




