# Project Euler Solutions
# Problem 007: 10001st prime
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 15:28, 21 June 2015
# https://github.com/v1neethnc/project-euler-solutions

# Since this is not a lot of computation, 10001st prime can be directly generated

def check(x):
	i = 2
	while i<=x//i:
		if x%i==0:
			return False
		i = i+1
	return True

co = 2
n = 3
while co!=10001:
	n = n+2
	if check(n):
		co = co+1
print(n)
