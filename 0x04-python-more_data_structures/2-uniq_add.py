#!/usr/bin/python3

def uniq_add(my_list=[]):
	"""adds all unique integers in a list
	(only once for each integer).
	"""

	_my_list = []

	for num in my_list:
		if num not in _my_list:
			sum += num
			_my_list.append(num)

	return sum
