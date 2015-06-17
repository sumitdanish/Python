__author__ = 'SU915198'

import sys
import os
import random


py_list = None


class MList:
	__n_data = 0
	__next_link = None

	def __init__(self, n_data, next_link):
		self.__n_data = n_data
		self.__next_link = next_link

	def __init__(self, n_data):
		self.__n_data = n_data

	@property
	def get_next_link(self):
		return self.__next_link

	def get_n_data(self):
		return self.__n_data

	def set_next_link(self, next_link):
		self.__next_link = next_link

	def set_n_data(self, n_data):
		self.__n_data = n_data


class CList:
	"""
		This method works for creation of linked list using recursion
		but printing order is reverse
	"""

	def create_my_list(self, n_data, next_link):
		n_link = MList(n_data, next_link)
		if next_link is None:
			next_link = n_link
			return next_link
		next_link.set_next_link(self.create_my_list(n_data, next_link.get_next_link()))
		return next_link

	def create_my_list1(self, n_data):
		"""
		This method create the list in the insertion order
		i.e it will print the list in the insertion order

		:param n_data:
		:return:
		"""
		n_link = MList(n_data)
		global py_list
		if py_list is None:
			py_list = n_link
		else:
			n1_link = py_list
			while n1_link.get_next_link is not None:
				n1_link = n1_link.get_next_link
			n1_link.set_next_link(n_link)

	@property
	def create_m_list(self):

		n_link = MList(1, None)
		n_link = MList(2, n_link)
		n_link = MList(3, n_link)
		n_link = MList(4, n_link)
		n_link = MList(5, n_link)
		return n_link

	@property
	def print_m_list(self):
		n_link = py_list
		while n_link is not None:
			print(n_link.get_n_data())
			n_link = n_link.get_next_link


if __name__ == "__main__":
	c_list = CList()
	"""
	
	list_file = open(os.path.relpath("list.txt"))
	 l_read = list_file.readline()
	ele_list = [l_data.strip("-->") for l_data in l_read]
	for l in list_file.read():
	print (l)

	c_list.create_my_list1(1)
	c_list.create_my_list1(2)
	c_list.create_my_list1(3)
	c_list.create_my_list1(4)
	c_list.create_my_list1(5)
	"""
	c_list.print_m_list