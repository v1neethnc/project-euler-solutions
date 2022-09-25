# Project Euler Solutions
# Problem 119: Digit power sum
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 16:06, 26 October 2020
# https://github.com/v1neethnc/project-euler-solutions

def digitSum(num):
	return sum([int(i) for i in str(num)])

vals = set()
for i in range(400):
	val = 1
	for j in range(30):
		val *= i
		if digitSum(val) == i:
			vals.add(val)
res = [i for i in vals if i > 9]
res.sort()
print(res[29])
