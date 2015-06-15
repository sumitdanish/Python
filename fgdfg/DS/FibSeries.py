__author__ = 'SU915198'


import sys
import random
import os


def fib(f_data):
	if f_data == 0 or f_data == 1:
		return 1
	return fib(f_data - 1) + fib(f_data - 2)



