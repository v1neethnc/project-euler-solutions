# Project Euler Solutions
# Problem 025: 1000-digit Fibonacci number
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 01:32, 17 May 2017
# https://github.com/v1neethnc/project-euler-solutions

# Generate fibonacci numbers and check the number of digits of each number.

def numdigits(x):
	s = 0
	while x>0:
		x = x//10
		s = s+1
	return(s)

f = 1
s = 1
n = 2
while True:
	t = f+s
	n = n+1
	r = numdigits(t)
	if r==1000:
		print(n)
		break
	f=s
	s=t
