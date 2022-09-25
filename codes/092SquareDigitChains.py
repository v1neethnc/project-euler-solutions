# Project Euler Solutions
# Problem 092: Square digit chains
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 23:44, 18 May 2017
# https://github.com/v1neethnc/project-euler-solutions

from itertools import combinations_with_replacement

def generate_first_element(num):
	vals = [int(i) for i in str(num)]
	vals.extend([0]*(7-len(vals)))
	vals.sort()
	return tuple(vals)

def fact_calc(num):
	res = 1
	while num > 1:
		res *= num
		num -= 1
	return res

list_89 = [(0,0,0,0,0,8,9)]
list_01 = [(0,0,0,0,0,0,1)]
res = combinations_with_replacement(range(10), 7)
res = [i for i in res]
for i in res[2:]:
	n = generate_first_element(sum([j**2 for j in i]))
	lst = [i]
	while n not in list_01:
		lst.append(n)
		if n in list_89:
			list_89.extend(lst)
			break
		n = generate_first_element(sum([j**2 for j in n]))
list_89 = set(list_89)
ctr = 0
for i in list_89:
	res_val = fact_calc(7)
	for j in set(i):
		temp = i.count(j)
		fact_val = fact_calc(temp)
		res_val = res_val // fact_val
	ctr += res_val
print(ctr)
