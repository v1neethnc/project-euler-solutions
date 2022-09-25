# Project Euler Solutions
# Problem 015: Lattice paths
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 18:28, 11 June 2017
# https://github.com/v1neethnc/project-euler-solutions

# This can be done using binomial coefficents. Using the formula:
# B(n, m) = (n+m)! / (n! * m!)
# the result can be determined.

def fact(x):
	f = 1
	for i in range(2,x+1):
		f = f*i
	return f

a = fact(40)
b = fact(20)
print(a//(b**2))
