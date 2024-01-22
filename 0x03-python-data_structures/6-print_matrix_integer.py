#!/usr/bin/python3

for col in range(len(matrix)):
	for row in range(len(matrix[col])):
		if row != 0:
			print(" ", end='')
		print("{:d}".format(matrix[col][row]), end='')
	print()
