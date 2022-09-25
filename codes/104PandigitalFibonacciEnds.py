# Project Euler Solutions
# Problem 104: Pandigital Fibonacci ends
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 20:20, 25 October 2020
# https://github.com/v1neethnc/project-euler-solutions

ctr = 3
f, s = 1, 1
while True:
	val = (f + s)% 1000000000
	if len(set(str(val))) == 9 and '0' not in set(str(val)):
		nm = str(f+s)
		if len(set(nm[:9])) == 9 and '0' not in set(nm[:9]):
			print(ctr)
			break
	ctr += 1
	f, s = s, f+s
