__author__ = 'SU915198'


import sys
import os
import random


class Error(Exception):
	"""
	Base class for other class
	"""
	pass


class ValueTooSmallError(Error):
	"""
	Exception will raise when value is too small
	"""
	pass


class ValueIsTooLargeError(Error):
	"""
	Exception will raise when value is too large
	"""
	pass


def my_exception():
	try:
		val1 = int(input("Enter first value : "))
		val2 = int(input("Enter second value :"))

		if val1 < val2:
			raise ValueTooSmallError
		elif val1 > val2:
			raise ValueIsTooLargeError
		else:
			print("You got it !:)")
	except ValueTooSmallError:
		print("Sorry ! value is too small : ")
	except ValueIsTooLargeError:
		print("Sorry ! value is too large :")
	finally:
		print('Execution is done !')


my_exception()