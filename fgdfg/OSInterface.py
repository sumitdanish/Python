__author__ = 'SUMMIT'

import os
import sys
import random


def os_my_interface():
	try:
		print("Current working directory %s" % os.getcwd())
		print("changing Working directory : ")
		#os.chdir("F:\\PythonWork")
		print("Current working directory after changing %s !" % os.getcwd())
		i = 0
		for my_dir_name in os.listdir(os.getcwd()):
			print(" {} : {}".format(i, my_dir_name))
			i = i+1
	except:
		print("Working directory is not exist %s " % sys.exc_info()[0])
	finally:
		print("Done !")















os_my_interface()