# Project Euler Solutions
# Problem 056: Powerful digit sum
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 01:27, 17 May 2017
# https://github.com/v1neethnc/project-euler-solutions

def sumof(x):
	s = 0
	while x>0:
		r = x%10
		x = x//10
		s = s+r
	return(s)

larg = 0
for a in range(1,100):
	for b in range(1,100):
		n = sumof(a**b)
		if n>larg:
			larg = n
print(larg)
