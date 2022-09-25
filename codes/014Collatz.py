# Project Euler Solutions
# Problem 014: Longest Collatz sequence
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 02:02, 17 May 2017
# https://github.com/v1neethnc/project-euler-solutions

# Function to generate the next number in the sequence.
# Consider the generated number and check the sequence length.
# Updating the maximum value each time a new max is encountered.

def collatz(x):
	co = 0
	while x!=1:
		if x%2==0:
			x = x/2
		else:
			x = 3*x+1
		co = co+1
	return co

n = 0
r = 0
for i in range(1,1000001):
	c = collatz(i)
	if n<c:
		n = c
		r = i
print(r)
