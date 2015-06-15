__author__ = 'SU915198'


import sys
import random
import os


def embed_one(x):
	def add_embed_one(y):
		return x+y
	return add_embed_one


# This variable a will return the function. for in above case it will return add_embed_one
# after that we will again pass the value again.

a = embed_one(2)
print(a(5))


