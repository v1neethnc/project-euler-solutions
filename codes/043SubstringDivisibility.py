# Project Euler Solutions
# Problem 043: Sub-string divisibility
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 20:13, 16 March 2020
# https://github.com/v1neethnc/project-euler-solutions

import itertools

def generate_pandigital(num):
	nms = [str(i) for i in range(0, num+1)]
	res = list(itertools.permutations(nms, r = num+1))
	final_res = []
	for i in res:
		if i[0] != '0':
			nm = ''
			for j in i:
				nm = nm + j
			final_res.append(nm)
	final_res = [i for i in final_res if int(i[1:4])%2 == 0 and int(i[2:5])%3 == 0 and int(i[3:6])%5 == 0]
	return final_res

final_data = []
list_data = generate_pandigital(9)
prm_nos = [7,11,13,17]
for val in list_data:
	nms = [int(val[i:i+3]) for i in range(4, 8)]
	ctr = 0
	for i in range(0, len(nms)):
		if nms[i] % prm_nos[i] == 0:
			ctr += 1
		else:
			break
	if ctr == len(prm_nos):
		final_data.append(int(val))
print(sum(final_data))
