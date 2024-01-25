#!/usr/bin/python3

def search_replace(my_list, search, replace):
	"""replaces all occurrences of an element by
	another in a new list
	@my_list: initial list
	@search: element to replace in the list
	@replace: the new element
	"""

	_my_list = []

	for item in my_list:	
		if item == search:
			_my_list.append(replace)
		else:
			_my_list.append(item)

	return _my_list
