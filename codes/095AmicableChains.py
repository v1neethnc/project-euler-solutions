# Project Euler Solutions
# Problem 095: Amicable chains
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 17:36, 26 October 2020
# https://github.com/v1neethnc/project-euler-solutions

lst = [0 for i in range(0, 1000001)]
for i in range(1, 500001):
	for j in range(i*2, 1000001, i):
		lst[j] += i

min_val, chain_len = 0, 0
for i in range(1, 1000001):
	checked_vals = []
	ind = i
	while True:
		val = lst[ind]
		if val > 1000000:
			break
		if ind in checked_vals:
			if ind == i:
				if len(checked_vals) > chain_len:
					min_val, chain_len = min(checked_vals), len(checked_vals)
			break
		else:
			checked_vals.append(ind)
			ind = val
print(min_val)
