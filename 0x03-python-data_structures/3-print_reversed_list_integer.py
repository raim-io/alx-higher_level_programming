#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
	reversed_list = my_list.reverse()
	for i in range(len(my_list) - 1):
		print(":d".format(reversed_list[i]))
