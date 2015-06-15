__author__ = 'SU915198'
import sys
import os
import random


class Fibonaci:

	def fibonaci_number(self, fibo):
		if fib == 0 or fibo == 1:
			return 1
		return fibo * self.fibonaci_number(fibo - 1)


print("Enter number : ")
num = int(sys.stdin.readline())
fib = Fibonaci()

fibnum = fib.fibonaci_number(num)
print('Fibonaci Number : ',fibnum)