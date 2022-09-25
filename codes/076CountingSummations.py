# Project Euler Solutions
# Problem 076: Counting summations
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 12:10, 04 June 2020
# https://github.com/v1neethnc/project-euler-solutions

total_req = 10
res = [1] + [0]*total_req
nums = [i for i in range(1, total_req)]
for num in nums:
	for i in range(num, total_req+1):
		res[i] += res[i - num]
print(res[total_req])
