# Project Euler Solutions
# Problem 074: Digit factorial chains
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 17:31, 31 October 2020
# https://github.com/v1neethnc/project-euler-solutions

lst = [0 for i in range(0, 1000001)]
fact_values = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
for i in range(0, len(lst)):
	nm = str(i)
	sm = 0
	for j in nm:
		sm += fact_values[int(j)]
	lst[i] = sm
ctr = 0
for i in range(0, 1000001):
	checked_vals = []
	ind = i
	while True:
		val = lst[ind]
		if val > 1000000:
			break
		if ind in checked_vals:
			if len(checked_vals) == 60:
				ctr += 1
			break
		else:
			checked_vals.append(ind)
			ind = val
print(ctr)
