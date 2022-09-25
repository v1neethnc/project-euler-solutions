# Project Euler Solutions
# Problem 033: Digit cancelling fractions
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 14:34, 15 March 2020
# https://github.com/v1neethnc/project-euler-solutions

from fractions import Fraction

def gcd(m,n):
	while (m%n) != 0:
		(m,n) = (n,m%n)
	return n

res = Fraction(1, 1)
for i in range(1, 100):
	for j in range(i+1, 100):
		nm_set, dm_set = set(str(i)), set(str(j))
		if i % 10 > 0 and j % 10 > 0 and len(nm_set) == 2 and len(dm_set) == 2 and gcd(i, j) > 1:
			if len(nm_set.intersection(dm_set)) == 1:
				common = nm_set.intersection(dm_set)
				nm_set = nm_set - common
				dm_set = dm_set - common
				if Fraction(i, j) == Fraction(int(nm_set.pop()), int(dm_set.pop())):
					res = res * Fraction(i, j)
print(res.denominator)
