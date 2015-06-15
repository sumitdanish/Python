__author__ = 'SU915198'
import os
import sys
import random


class Fridge:
	__item_list = {}
	__food_name = {}
	__quantity = 0

	def __init__(self, item_list):
		if type({}) != type(item_list):
			raise TypeError("Fridge require dictionary but u have give the String name %s" % type(item_list))
		self.__item_list = item_list

	def add_food_name(self, food_name):
		if type(food_name) != type(""):
			raise TypeError("Add food name in from of String %s" % (type(food_name)))
		self.__add_food_item_list(food_name, 1)

	def add_food_item(self, food_list):
		if type(food_list) != type({}):
			raise TypeError("Please enter the list of the food")
		else:
			for item in food_list.keys():
				self.__add_food_item_list(item, food_list[item])

	def __add_food_item_list(self, food_name, quantity):
		if not food_name in self.__item_list:
			self.__item_list[food_name] = 0
			print("The enter food_name %s is not exist" % food_name)
		else:
			self.__item_list[food_name] = self.__item_list[food_name] + quantity


	@property
	def get_quantity(self):
		return self.__quantity

	def set_quantity(self, quantity):
		self.__quantity = quantity

	@property
	def get_items_list(self):
		return self.__item_list

	def set_item_list(self, item_list):
		self.__item_list = item_list

	@property
	def get_food_name(self):
		return self.__food_name

	def set_food_name(self, food_name):
		self.__food_name = food_name

# if __name__ == "__main__":
details = {'Name': 1, 'Age': 7, 'Class': 3}
obj = Fridge(details)
# obj.add_food_name("Orange")
obj.add_food_item({'Age': 3, 'eggs': 6, 'grape': 1, 'milk': 4})
print(sorted(details.keys()))
for item_name in obj.get_items_list.keys():
	print('Item name : {} and value of the item Name {}'.format(item_name, details[item_name]))

"""
The below loop is for unpacking the dictionary by key and value pair

for k, v in obj.get_items_list.items():
	print('Item name : {} and value of the item Name {}'.format(k, v))
"""