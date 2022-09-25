# Project Euler Solutions
# Problem 348: Sum of a square and a cube
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 14:24, 26 October 2020
# https://github.com/v1neethnc/project-euler-solutions

from math import sqrt

def isSquare(num):
	if num % 10 in [2, 3, 7, 8]:
		return False
	return str(sqrt(num))[-2:] == '.0'

def gen_palindromes(n):
	lim = 10 ** (n//2) if n % 2 == 0 else 10 ** ((n+1)//2)
	nums = [str(i) for i in range(lim)]
	if n %2 == 0:
		nums = [int(i + i[::-1]) for i in nums if len(i + str(i)) == n]
	else:
		nums = [int(i + i[-2::-1]) for i in nums if len(i + i[-2::-1]) == n]
	return nums

ctr, n, sm = 0, 7, 0
while ctr != 5:
	vals = gen_palindromes(n)
	for i in vals:
		temp_ctr = 0
		for j in range(1, round(i ** (1/3))):
			if isSquare(i - (j*j*j)):
				temp_ctr += 1
				if temp_ctr == 5:
					break
		if temp_ctr == 4:
			sm += i
			ctr += 1
			if ctr == 5:
				print(sm)
				break
	n += 1
