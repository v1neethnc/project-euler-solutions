# Project Euler Solutions
# Problem 048: Self powers
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 01:22, 17 May 2017
# https://github.com/v1neethnc/project-euler-solutions

s = 0
for i in range(1,1001):
	s = (s+(i**i))%(10**10)
print(s)
