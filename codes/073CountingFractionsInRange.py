# Project Euler Solutions
# Problem 073: Counting fractions in a range
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 16:00, 22 October 2020
# https://github.com/v1neethnc/project-euler-solutions

def gcd(m,n):
	while (m%n) != 0:
		(m,n) = (n,m%n)
	return n
set_frac = set()
for d in range(5, 12001):
	for n in range(d//3+1, (d-1)//2+1):
		if n == 0:
			continue
		gcd_val = gcd(n, d)
		fr = str(n//gcd_val) + '/' + str(d//gcd_val)
		set_frac.add(fr)
print(len(set_frac))
