# Project Euler Solutions
# Problem 001: Multiples of 3 or 5
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 14:54, 20 June 2015
# https://github.com/v1neethnc/project-euler-solutions

# Checking if encountered number is multiple of 3 or 5.
# If true, adding the number to the sum variable.

sum = 0
for i in range(1,1000):
	if i%3==0 or i%5==0:
		sum += i
print(sum)
