from tkinter import *

import sys
import os
import random
import pymysql.connections
ctx=pymysql.connections
print('Enter your name : ')
name = sys.stdin.readline()
print('Hello ', name)