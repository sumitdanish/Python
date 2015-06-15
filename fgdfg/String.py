import sys
import os
import random

long_string='hey due Where 1234 Are you right now ?         '
print(long_string[0:4])
print(long_string[:4])
print(long_string[:-5])
print(long_string[0:-5])
#print(long_string[-5:0])#it will not work
print(long_string[-5:])
print(long_string[-5:],' so sweet')
print(len(long_string))


print(long_string.capitalize())
print(long_string.isalpha())
print(long_string.isalnum())
print(long_string.replace("?","WIPRO"))
print(len(long_string.strip()))
list = long_string.strip().split(" ")
print(list)