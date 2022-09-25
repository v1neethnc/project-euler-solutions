# Project Euler Solutions
# Problem 010: Summation of primes
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 16:29, 29 June 2015
# https://github.com/v1neethnc/project-euler-solutions

# Function to check if a given number is prime or not.
# Using this function, generate primes under 2 million and calculate the sum.

def check(x):
	i = 3
	while i<=x//i:
		if x%i==0:
			return False
			break
		i = i+2
	return True

su = 2
i = 3
while i<2000000:
	if check(i):
		su = su+i
	i = i+2
print(su) 
