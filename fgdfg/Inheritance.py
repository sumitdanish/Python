__author__ = 'SU915198'
import sys
import os
import random

class ColorOne:
	__color = None

	def set_color(self, color):
		self.__color = color

	def get_color(self):
		return self.__color

	def __init__(self, color='green'):
		self.__color = color

	def hello(self):
		print('Calling from classOne'.format(self.__color))


class ColorTwo(ColorOne):
	__color_one = None

	def set_color_one(self, color_one):
		self.__color_one = color_one

	def get_color_one(self):
		return self.__color_one

	def __init__(self, color_one='Red'):
		self.__color_one = color_one

	def hello_form_two(self):
		print('HelloFromTwo {} '.format(self.__color_one))


col1 = ColorOne()
col1.hello()

col2 = ColorTwo()
col2.hello_form_two()
col1.hello()
