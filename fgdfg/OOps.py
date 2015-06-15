__author__ = 'SU915198'
import sys
import os
import random


class EmployeeP:
	__name = None
	__position = None
	__rank = 0
	__basic = 0

	def set_name(self, name):
		self.__name = name

	def set_rank(self, rank):
		self.__rank = rank

	def set_position(self, position):
		self.__position = position

	def set_basic(self, basic):
		self.__basic = basic

	def __init__(self, name, position, rank):
		self.__name = name
		self.__position = position
		self.__rank = rank
		if self.__rank == 1:
			self.set_basic(1000000)
		elif self.__rank == 2:
			self.set_basic(12345)
		else:
			self.set_basic(12321)

	def __eq__(self, other):
		if self.__rank == other.__rank and self.__position == other.__position:
			return True

	def __str__(self):
		return 'Employee {} got basic amount of ${} on the basis of his rank {}'.format(self.__name, self.__basic, self.__rank)


emp = EmployeeP('SUMMIT', 'SDE2', 1)
emp1 = EmployeeP('SUMMIT KES', 'SDE2', 1)

print(emp)
print(emp1)

if emp == emp1:
		print('Object are equal')
else:
	print('Object are not equal')
