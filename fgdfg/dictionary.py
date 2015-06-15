import sys
import os
import random

villian = {'123':'SUMIT',
		   '124':'SUMMIT',
		   '125':'Python',
		   '126':'cobra',
		   '127':'luliya'}
		   
print(villian)
del villian['123']
print(villian)
villian['125']='Python cobra'
print(villian.get('127'))
print(villian.keys())
print(villian.values())


tabby_cat = "\t i am tabbed in."
persian_cat = "I am split\non a line"
backlash_cat = "I'm \\ a \\ cat"
fat_cat = """
		 i'll do this:
		 \t* Cat food
		 \t* cat mile
		 \t* cat dance
		 \t* catnip \n\t* Grass
		 """

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)


