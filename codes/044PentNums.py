# Project Euler Solutions
# Problem 044: Pentagon numbers
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 20:03, 15 March 2020
# https://github.com/v1neethnc/project-euler-solutions

from math import sqrt, floor, ceil

def is_pentagonal(num):
	res = (1 + sqrt(1 + 4*3*2*num)) / (2*3)
	return floor(res) == ceil(res)

i = 1
notFound = True
while notFound:
	val1 = (i * (3*i - 1) // 2)
	for j in range(i-1, 0, -1):
		val2 = (j * (3*j - 1) // 2)
		if is_pentagonal(val1 + val2) and is_pentagonal(val1 - val2):
			print(val1 - val2)
			notFound = False
			break
	i += 1
