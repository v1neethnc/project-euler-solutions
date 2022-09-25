# Project Euler Solutions
# Problem 046: Goldbach's other conjecture
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 20:17, 15 March 2020
# https://github.com/v1neethnc/project-euler-solutions

from math import sqrt, floor, ceil

def check(x):
	i = 2
	while i<=x//i:
		if x%i==0:
			return False
		i = i+1
	return True

i = 7
notFound = True
while notFound:
	i += 2
	if not check(i):
		possible = False
		j = 2
		while j < i:
			if check(j):
				res = sqrt((i - j) / 2)
				if floor(res) == ceil(res):
					possible = True
					break
			j = j+2 if j != 2 else j+1
		if possible == False:
			notFound = False
print(i)
