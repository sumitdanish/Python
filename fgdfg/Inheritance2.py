__author__ = 'SU915198'
import sys
import random
import os


class Polygon:
	__no_of_side = 0
	__side = []

	def __init__(self, no_of_side):
		self.__no_of_side = no_of_side
		self.__side = [0 for i in range(no_of_side)]

	def set_side(self):
		self.__side = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.__no_of_side)]

	def get_side(self):
		return self.__side;

	def display_side(self):
		for i in range(self.__no_of_side):
			print("Enter side {}".format(self.__side[i+1]))


class Triangle(Polygon):

	__area = 0
	__semi_parameter = 0

	def __init__(self):
		Polygon.__init__(self, 3)

	def set_area(self, area):
		self.__area = area

	def get_area(self):
		return self.__area

	def find_area(self):
		a, b, c = self.get_side()
		self.__semi_parameter = (a+b+c)*0.50
		s = self.__semi_parameter
		a = float((s*(s-a)*(s-b)*(s-c))**0.50)
		print("Area of the triangle : %0.2f" % a)


triangle = Triangle()
triangle.set_side()
triangle.find_area()

