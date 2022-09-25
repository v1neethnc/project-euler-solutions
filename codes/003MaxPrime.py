# Project Euler Solutions
# Problem 003: Largest prime factor
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 16:12, 20 June 2015
# https://github.com/v1neethnc/project-euler-solutions

# Like every number, the given number is a product of a unique set of prime numbers.
# Here, the number is factored and the range to check is reduced by dividing the upper
# limit with the obtained factor. This will reduce the number of iterations. This process
# will be repeated until such a time where the upper limit and the obtained factor are either
# equal or the upper limit is equal to 1. This implies that none of the numbers other than the
# obtained factor can divide the new upper limit, which in turn implies that the obtained factor
# is the only number that can divide the new upper limit.

ch = 0
n = 600851475143
for i in range(2,n+1):
	while n%i==0:
		n = n//i
		if n==i or n==1:
			print(i)
			ch=1
			break
	if ch==1:
		break
