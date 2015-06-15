__author__ = 'SU915198'
import sys
import os
import random


class LinkList(object):
	__data = 0
	__next_link = None

	def __init__(self, data):
		self.__data = data


	def set_next_link(self, next_link):
		self.__next_link = next_link

	def get_next_link(self):
		return self.__next_link

	def set_data(self, data):
		self.__data = data

	def get_data(self, data):
		return self.__data


# noinspection PyArgumentList
class FileIO(object):
	def file_reading(self, file_name):
		test_file = open(file_name, "r+")
		file_con = test_file.read()
		element_in = [line.strip("-->") for line in file_con]
		return element_in

	def create_list(self, data, link_list):
		if link_list is None:
			link_list = LinkList(data)
			return link_list
		link_list.set_next_link(self.create_list(data, link_list.get_next_link()))

	def print_list(self, link_list: LinkList):
		my_list1 = link_list
		print(my_list1.get_data())
		while my_list1 is not None:
			print(my_list1.get_data(), end="")
			my_list1 = my_list1.get_next_link()


file_io = FileIO()
my_list = None
for data1 in file_io.file_reading('list.txt'):
	my_list = file_io.create_list(data1, my_list)

file_io.print_list(my_list)

