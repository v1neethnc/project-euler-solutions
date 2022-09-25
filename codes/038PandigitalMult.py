# Project Euler Solutions
# Problem 038: Pandigital multiples
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 23:06, 15 March 2020
# https://github.com/v1neethnc/project-euler-solutions

ans = 0
for i in range(1, 50000):
	st_nm = set(str(i))
	res = str(i)
	if len(st_nm) == len(str(i)):
		j = 2
		while len(st_nm) < 9 and '0' not in st_nm:
			nm_new = str(i * j)
			if len(st_nm.intersection(set(nm_new))) == 0 and '0' not in set(nm_new):
				st_nm = st_nm.union(set(nm_new))
				res = res + nm_new
			else:
				break
			j += 1
		if len(st_nm) == len(res) and int(res) > ans:
			ans = int(res)
print(ans)
