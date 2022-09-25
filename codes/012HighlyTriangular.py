# Project Euler Solutions
# Problem 012: Highly divisible triangular number
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 15:23, 02 December 2016
# https://github.com/v1neethnc/project-euler-solutions

# Beginning the search at 28 as it is already given in the question.
# Generate a new triangular number with each iteration.
# For each triangular number, calculate the number of divisors.
# If the number of divisors exceeds 500, break out of the loop.

n = 28
i = 8
while True:
	n = n+i
	i = i+1
	c = 2
	j = 2
	while(j*j<=n):
		if n%j==0:
			c = c+2
		j = j+1
	if c>500:
		print(n)
		break
