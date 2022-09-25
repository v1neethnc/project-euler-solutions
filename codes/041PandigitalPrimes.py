# Project Euler Solutions
# Problem 041: Pandigital prime
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 17:07, 15 March 2020
# https://github.com/v1neethnc/project-euler-solutions

import itertools

def check(x):
	i = 2
	while i<=x//i:
		if x%i==0:
			return False
		i = i+1
	return True

def generate_pandigital(num):
	nms = [str(i) for i in range(1, num+1)]
	return list(itertools.permutations(nms, r = num))

i = 9
max_val = 0
while i > 0:
	nm_lst = generate_pandigital(i)
	for nm in nm_lst:
		number = ''
		for j in nm:
			number = number + str(j)
		if check(int(number)):
			if max_val < int(number):
				max_val = int(number)
	i = i -1
print(max_val)
