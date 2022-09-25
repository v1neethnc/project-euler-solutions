# Project Euler Solutions
# Problem 049: Prime permutations
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 23:43, 15 March 2020
# https://github.com/v1neethnc/project-euler-solutions

from itertools import permutations

def check(x):
	i = 2
	while i<=x//i:
		if x%i==0:
			return False
		i = i+1
	return True

def get_permutations(x):
	res = list(permutations(str(x), r = len(str(x))))
	final_res = set()
	for i in res:
		st = ''
		for j in i:
			st = st + j
		if st[0] != '0':
			final_res.add(int(st))
	final_res = sorted(final_res)
	return final_res

sols = []
for i in range(1488, 10000):
	if check(i):
		permutes = get_permutations(i)
		rs = set()
		for j in permutes:
			if check(j):
				rs.add(j)
		if len(rs) > 2:
			rs = sorted(rs)
			c = 0
			tmp_set = set()
			for tmp in rs:
				if tmp+3330 in rs:
					c += 1
					tmp_set.add(tmp)
					tmp_set.add(tmp+3330)
			if c == 2 and list(sorted(tmp_set)) not in sols:
				sols.append(list(sorted(tmp_set)))
			tmp_set.clear()

prime_permt = ''            
for i in sols:
	if 1487 not in i:
		prime_permt = str(i[0]) + str(i[1]) + str(i[2])
print(prime_permt)
