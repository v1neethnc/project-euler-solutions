# Project Euler Solutions
# Problem 020: Factorial digit sum
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 00:59, 17 May 2017
# https://github.com/v1neethnc/project-euler-solutions

# This can be made simpler using a sieve, but as of now, the result
# is calcualted by generating all the factorials and then calculating the
# sum. The sum calculation itself can be sped up by converting the number
# to a list and then using the sum function.

def factorial(x):
	fact = 1
	for i in range(2,x+1):
		fact = fact * i
	return(fact)

def sumof(x):
	s = 0
	while x>0:
		r = x%10
		x = x//10
		s = s+r
	return(s)

print(sumof(factorial(100)))
