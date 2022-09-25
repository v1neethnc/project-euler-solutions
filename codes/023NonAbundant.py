# Project Euler Solutions
# Problem 023: Non-abundant sums
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 13:19, 20 June 2017
# https://github.com/v1neethnc/project-euler-solutions

# A function to calcualte the sum of divisors.
# First, creating a list of all the abundant numbers under 28123.
# Next, generating all numbers that are sum of two abundant numbers.
# Calculating the difference between the total possible sum under 28123 and the newly generated list.

import math
def divisorCalc(x):
	y = int(math.sqrt(x))
	s = 0
	if y*y==x:
		s += y
	else:
		y += 1
	for i in range(2,y):
		if x%i==0:
			s = s+i+(x//i)
	return s

abun = []
for i in range(12,28124):
	s = divisorCalc(i)
	if s>i:
		abun.append(i)

abunsum = []
for i in range(0,len(abun)):
	for j in range(i,len(abun)):
		x = abun[i]+abun[j]
		if x<28124:
			abunsum.append(x)
		else:
			break
x = set(abunsum)
y = 28123*28124//2
print(y-sum(x))
