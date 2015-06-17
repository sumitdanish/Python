__author__ = 'SU915198'

import sys
import os
import random


def my_lambda_exp():
	#filter_me = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	map_me = ['a', 'a', 'c', 'd', 'e', 'f']
	map_result = map(lambda x: "You are printing the character %s \n " % x, map_me)
	map_list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	map_result_list = map(lambda list: [list[0], list[1], list[2]], map_list_of_list)
	#result = filter(lambda x: x % 2 == 0, filter_me)
	print(*map_result_list)

my_lambda_exp()