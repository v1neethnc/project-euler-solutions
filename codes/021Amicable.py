# Project Euler Solutions
# Problem 021: Amicable numbers
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 17:27, 22 December 2015
# https://github.com/v1neethnc/project-euler-solutions

# A function to calculate and return the sum of factors.
# A list to store the numbers already checked.
# For each number, find the sum of factors.
# Find the sum of factors for the sum of factors of the first number.
# If match, add to the list.
# This can be sped up using a sieve where the sum of factors of each number
# are generated and stored in a list.

def factsum(x):
	s = 0
	e = x//2
	for i in range(1,e+1):
		if x%i==0:
			s = s+i
	return s
li = []
s = 0
for i in range(11,10000):
	if i not in li:
		n = factsum(i)
		x = factsum(n)
		if i==x and i!=n:
			li.append(i)
			li.append(n)
			s = s+i+n
print(s)
