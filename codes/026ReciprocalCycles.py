# Project Euler Solutions
# Problem 026: Reciprocal cycles
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 18:23, 20 June 2017
# https://github.com/v1neethnc/project-euler-solutions

# Start off backwards from 1000, maintain a list of remainders.
# Append each remainder to the list as long as they're not present.
# If the number of remainders is one less than the actual number, then it will 
# automatically be the maximum value.

for i in range(999,0,-1):
	rem = []
	e = 1
	ch = 0
	while True:
		r = e%i
		if r not in rem:
			rem.append(r)
			e = r*10
		else:
			x = len(rem)
			if x == i-1:
				print(i)
				ch = 1
			break
	if ch==1:
		break
