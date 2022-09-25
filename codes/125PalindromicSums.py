# Project Euler Solutions
# Problem 125: Palindromic sums
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 19:14, 02 November 2020
# https://github.com/v1neethnc/project-euler-solutions

from math import sqrt
def isPalindrome(n):
	return str(n) == str(n)[::-1]

vals_set = []
sm = 0
for i in range(1, 10000):
	tmp_sm = i*i
	for j in range(i+1, 10001):
		tmp_sm += (j*j)
		if tmp_sm > 10**8:
			break
		if isPalindrome(tmp_sm) and tmp_sm not in vals_set:
			vals_set.append(tmp_sm)
			sm += tmp_sm
print(sm)
