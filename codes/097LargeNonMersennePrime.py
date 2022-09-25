# Project Euler Solutions
# Problem 097: Large non-Mersenne prime
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 02:26, 16 March 2020
# https://github.com/v1neethnc/project-euler-solutions

val = 1
for i in range(1, 7830458):
	val = (val * 2) % (10000000000)
print((28433 * val + 1)% (10000000000))
