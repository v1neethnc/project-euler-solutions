# Project Euler Solutions
# Problem 047: Distinct primes factors
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 22:29, 15 March 2020
# https://github.com/v1neethnc/project-euler-solutions

from math import sqrt, floor, ceil

def check(x):
	i = 2
	while i <= x//i:
		if x%i == 0:
			return False
		i += 1
	return True

def prime_factors(x):
	i = 3
	factors = []
	while x % 2 == 0:
		factors.append(2)
		x = x // 2
	while i <= x:
		while x % i == 0:
			factors.append(i)
			x = x // i
		i = i+2
	return set(factors)

notFound = True
i = 16
ctr = 0
res = -1
while True:
	if not check(i) and len(prime_factors(i)) == 4:
		if ctr == 0:
			res = i
		ctr += 1

	elif ctr < 4:
		ctr = 0
	if ctr == 4:
		print(res)
		break
	i += 1
