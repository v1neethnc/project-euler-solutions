# Project Euler Solutions
# Problem 029: Distinct powers
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 01:05, 17 May 2017
# https://github.com/v1neethnc/project-euler-solutions

li = []
for a in range(2,101):
	for b in range(2,101):
		n = a**b
		if n not in li:
			li.append(n)
			li.sort()
print(len(li))
