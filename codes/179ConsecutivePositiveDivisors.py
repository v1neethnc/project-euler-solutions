# Project Euler Solutions
# Problem 179: Consecutive positive divisors
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 14:16, 28 October 2020
# https://github.com/v1neethnc/project-euler-solutions

lst = [2 for i in range(10000000)]
for i in range(2, len(lst)//2+1):
	for j in range(2*i, len(lst), i):
		lst[j] += 1
ctr = 0
for i in range(2, len(lst) - 1):
	if lst[i] == lst[i+1]:
		ctr += 1
print(ctr)
