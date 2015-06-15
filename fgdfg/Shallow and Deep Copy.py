__author__ = 'SU915198'
import sys
import random
import os
from copy import deepcopy
'''
Shallow copy concept
list1=['asdf','jhsgdf','jhsgdf']
list2=list1;
print(id(list1),id(list2))

list2[1] = 'iuer'
print(list1,list2)'''


list1=['Summit','Sumeet','SumitKu',['yes','no','other','Fcuk',]]

list2=list1[:]
list2[1]='Hey man!'
print(list2)
#print(id(list1),id(list2))
list2[3][3] = 'So sorry!'
print(list1)
print(list2)

#Deep copy after importing deepcopy module

list2 = deepcopy(list1)
list2[1]='oi'
list2[3][1] = 'Its Possible !'
print(list1)
print(list2
)
