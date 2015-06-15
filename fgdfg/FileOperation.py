from Tools.Scripts.treesync import create_files

__author__ = 'SUMMIT'

import sys
import random
import os


class FileAction:
	__file_name = ""
	__file_content = ""
	__file_object = None
	def set_file_content(self,f_content):
		self.__file_content = f_content

	def get_file_content(self):
		return self.__file_content

	def get_file_name(self):
		return self.__file_name;

	def set_file_name(self, f_name):
		self.__file_name = f_name

	@property
	def create_file(self):
		is_file_create = False
		if os.path.isfile(self.get_file_name()):
			is_file_create = False;
			raise TypeError("you are trying to create new file")
		else:
			is_file_create = True
			f = open(self.get_file_name(), 'w')
		return is_file_create

	def file_event(self, f_name):
		if not self.create_file(self):
			raise TypeError ("FIle operation done !")
		#else:


if __name__ == "__main__":
	is_file_create = False
	fi_name = input('Enter file name : ')
	file_operation = FileAction()
	file_operation.set_file_name(fi_name)
	print("File name : %s : " % file_operation.get_file_name())
	f = file_operation.create_file()





